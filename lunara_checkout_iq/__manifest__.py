# -*- coding: utf-8 -*-
{
    "name": "Iraq Checkout for Odoo 19",
    "version": "19.0.2.1.0",
    "summary": "Configurable checkout email/phone requirements and Iraqi +964 phone normalization.",
    "author": "Lunara Iraq",
    "website": "https://github.com/lulu1935lulu1-design/-odoo19-iraq-checkout",
    "category": "Website/Website",
    "license": "LGPL-3",
    "depends": [
        "website_sale",
        "phone_validation",
    ],
    "data": [
        "res_config_settings_views.xml",
        "checkout_address_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
