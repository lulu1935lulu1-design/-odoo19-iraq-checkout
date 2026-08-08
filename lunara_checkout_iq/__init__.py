# -*- coding: utf-8 -*-
"""Iraq-focused checkout helpers for Odoo 19."""

import logging
import re

from odoo import api, fields, models, _
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.exceptions import ValidationError
from odoo.http import request

_logger = logging.getLogger(__name__)

IQ_CC = "964"
_IQ_VALID_RE = re.compile(r"^\+964\d{8,11}$")


class Website(models.Model):
    _inherit = "website"

    lunara_checkout_email_required = fields.Boolean(
        string="Require email at checkout",
        default=False,
        help="Off: customers can check out with name and phone only "
        "(email optional). On: email becomes mandatory.",
    )
    lunara_checkout_phone_required = fields.Boolean(
        string="Require phone at checkout",
        default=True,
        help="Strongly recommended for Cash on Delivery so every order "
        "carries a contact number.",
    )
    lunara_checkout_required_fields = fields.Char(
        compute="_compute_lunara_checkout_required_fields",
    )

    @api.depends("lunara_checkout_email_required", "lunara_checkout_phone_required")
    def _compute_lunara_checkout_required_fields(self):
        for site in self:
            names = ["name"]
            if site.lunara_checkout_phone_required:
                names.append("phone")
            if site.lunara_checkout_email_required:
                names.append("email")
            site.lunara_checkout_required_fields = ",".join(names)


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    lunara_checkout_email_required = fields.Boolean(
        related="website_id.lunara_checkout_email_required",
        readonly=False,
        string="Require email at checkout",
    )
    lunara_checkout_phone_required = fields.Boolean(
        related="website_id.lunara_checkout_phone_required",
        readonly=False,
        string="Require phone at checkout",
    )


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _lunara_normalize_iq_number(self, number):
        if not number:
            return number
        original = number
        s = str(number).strip()
        had_plus = s.startswith("+")
        digits = re.sub(r"\D", "", s)
        if not digits:
            return original

        if digits.startswith("00964"):
            nsn = digits[5:]
        elif digits.startswith(IQ_CC):
            nsn = digits[len(IQ_CC) :]
        elif had_plus:
            return "+" + digits
        elif digits.startswith("00"):
            return "+" + digits[2:]
        else:
            nsn = digits

        nsn = nsn.lstrip("0")
        if not nsn:
            return original

        if len(nsn) == 10 and nsn.startswith("7"):
            return "+%s%s" % (IQ_CC, nsn)
        if 8 <= len(nsn) <= 11:
            return "+%s%s" % (IQ_CC, nsn)

        return original

    def _lunara_apply_phone_normalization(self, vals):
        if vals.get("phone"):
            vals["phone"] = self._lunara_normalize_iq_number(vals["phone"])
        return vals

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            self._lunara_apply_phone_normalization(vals)
        return super().create(vals_list)

    def write(self, vals):
        if vals.get("phone"):
            vals = dict(vals)
            self._lunara_apply_phone_normalization(vals)
        return super().write(vals)

    @api.constrains("phone")
    def _lunara_check_iq_phone(self):
        for partner in self:
            number = partner.phone
            if not number:
                continue
            compact = re.sub(r"\s+", "", number)
            if compact.startswith("+") and not compact.startswith("+964"):
                continue
            if not _IQ_VALID_RE.match(compact):
                raise ValidationError(
                    _(
                        "“%s” is not a valid Iraqi phone number.\n"
                        "Enter it as 07XX XXX XXXX or +964 7XX XXX XXXX."
                    )
                    % number
                )


class LunaraWebsiteSaleCheckout(WebsiteSale):
    def _get_mandatory_address_fields(self, *args, **kwargs):
        fields_set = super()._get_mandatory_address_fields(*args, **kwargs)
        try:
            fields_set = set(fields_set or [])
            website = getattr(request, "website", None)
            email_required = bool(website and website.lunara_checkout_email_required)
            phone_required = website.lunara_checkout_phone_required if website else True

            if email_required:
                fields_set.add("email")
            else:
                fields_set.discard("email")

            if phone_required:
                fields_set.add("phone")
            else:
                fields_set.discard("phone")
        except Exception:
            _logger.debug(
                "lunara_checkout_iq: could not adjust mandatory fields",
                exc_info=True,
            )
        return fields_set
