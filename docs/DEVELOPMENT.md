# Development and Testing Guide

This document is for contributors working on Iraq Checkout for Odoo 19.

## Prerequisites

Use a legitimate Odoo 19 development/test environment with these add-ons available:

- `website_sale`
- `phone_validation`

This public repository does not provide Odoo Enterprise source code or a prebuilt proprietary environment.

## Local layout

A typical development layout is:

```text
custom-addons/
└── lunara_checkout_iq/
    ├── __init__.py
    ├── __manifest__.py
    ├── checkout_address_views.xml
    ├── res_config_settings_views.xml
    └── tests/
```

Add the repository/module path to your Odoo `addons_path` using your normal development setup.

## Clean install test

Use a disposable test database. A typical Odoo command is:

```bash
odoo-bin \
  -d odoo19_iraq_checkout_test \
  -i lunara_checkout_iq \
  --test-enable \
  --stop-after-init
```

If your Odoo executable/configuration differs, adapt the command without changing the test intent.

## Module-specific tests

A typical module-targeted run is:

```bash
odoo-bin \
  -d odoo19_iraq_checkout_test \
  -u lunara_checkout_iq \
  --test-enable \
  --test-tags /lunara_checkout_iq \
  --stop-after-init
```

## Upgrade test

Always test updates against a database where the previous public version is already installed:

```bash
odoo-bin \
  -d odoo19_iraq_checkout_upgrade_test \
  -u lunara_checkout_iq \
  --test-enable \
  --stop-after-init
```

An upgrade test should confirm at minimum:

- module registry loads successfully;
- website settings remain readable;
- checkout address page renders;
- existing partners remain valid;
- new/updated Iraqi phone values normalize as intended.

## Public CI scope

The GitHub Actions workflow in this repository intentionally avoids downloading or redistributing proprietary Odoo code. It checks:

- Python syntax compilation;
- XML well-formedness;
- expected repository structure;
- basic protection against accidentally committed sensitive file types.

That public CI is useful, but it is **not a substitute for Odoo runtime tests**.

## Manual checkout regression checklist

On a disposable Odoo 19 test site, check:

1. Email optional + phone required.
2. Email required + phone required.
3. Email optional + phone optional.
4. Local Iraqi phone input such as `0770 123 4567`.
5. Existing `+964...` input.
6. A valid non-Iraqi international number.
7. Invalid/too-short Iraqi input.
8. Guest checkout.
9. Logged-in customer checkout.
10. Multiple Website configurations if the environment uses multi-website.

## Before submitting a PR

Record the exact Odoo version/build, exact test command, exit code, and any failures. Never hide unrelated failures; distinguish them clearly from module regressions.
