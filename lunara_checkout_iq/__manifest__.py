# -*- coding: utf-8 -*-
{
    "name": "Iraq Checkout for Odoo 19",
    "version": "19.0.2.1.0",
    "summary": "Odoo 19 compatible checkout controls and Iraqi +964 phone normalization.",
    "description": (
        "Open-source Odoo 19 checkout enhancements for Iraqi e-commerce. "
        "Maintained by Lunara Iraq — https://lunara.com.iq — info@lunara.com.iq"
    ),
    "author": "Lunara Iraq",
    "maintainer": "Lunara Iraq",
    "website": "https://lunara.com.iq",
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
