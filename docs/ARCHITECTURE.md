# Architecture

## Purpose

Iraq Checkout for Odoo 19 is intentionally a small extension of Odoo's existing website checkout and partner models. It does not replace Odoo's checkout engine.

## Main extension points

### `website`

Adds per-website policy fields:

- `lunara_checkout_email_required`
- `lunara_checkout_phone_required`
- computed `lunara_checkout_required_fields`

The computed field is used by the website checkout template to communicate required fields to Odoo's normal checkout flow.

### `res.config.settings`

Exposes the Website policy fields through standard Odoo settings using related fields.

### `res.partner`

Adds deterministic Iraqi phone normalization before partner create/write and validates Iraqi-formatted values.

The design preserves numbers that are explicitly international and non-Iraqi rather than forcing all phone numbers into `+964`.

### `WebsiteSale`

Extends `_get_mandatory_address_fields()` so Odoo's own checkout validation respects the configured email/phone policy.

### QWeb/XML views

The inherited checkout template:

- supplies the computed required-field list;
- changes required/optional label classes;
- adds an Iraqi phone placeholder and telephone input mode.

## Data flow

```text
Website Settings
      │
      ▼
website policy fields
      │
      ├──────────────► required_fields in checkout form
      │
      └──────────────► WebsiteSale mandatory-field decision
                             │
                             ▼
                      Odoo normal checkout
                             │
                             ▼
                         res.partner
                             │
                             ▼
                   phone normalization/validation
```

## Security boundaries

The module should remain independent of:

- payment gateway credentials;
- customer exports;
- database backup files;
- external tracking services;
- proprietary Odoo Enterprise source code.

New external network dependencies require explicit design review and documentation.

## Compatibility policy

The public `main` branch targets Odoo 19. Changes that depend on version-specific private/proprietary code should not be merged.

## Naming note

The technical module and some field identifiers retain the historical `lunara_` namespace for compatibility with existing installations. Public-facing documentation describes the project generically as Iraq Checkout for Odoo 19. Renaming database field identifiers would require a deliberate migration rather than a cosmetic code edit.
