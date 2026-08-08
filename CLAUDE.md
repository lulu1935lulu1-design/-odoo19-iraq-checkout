# Claude Code Project Context

This file gives AI-assisted contributors a concise, repository-specific operating guide.

## Project

Iraq Checkout for Odoo 19 is a small open-source Odoo add-on for configurable checkout email/phone requirements and Iraqi `+964` phone normalization.

## Hard boundaries

- Target Odoo 19 unless a task explicitly says otherwise.
- Never add or copy Odoo Enterprise source code into this repository.
- Never commit credentials, API tokens, private keys, database dumps, customer data, production logs, `.env` files, or session files.
- Do not invent external API integrations for this module.
- Do not silently change stored field identifiers with the historical `lunara_` namespace; that would require a migration plan.
- Prefer Odoo extension points over monkey-patching.
- Keep behavior configurable and reusable; avoid merchant-specific hardcoding.

## Important files

- `lunara_checkout_iq/__manifest__.py` — module metadata/dependencies.
- `lunara_checkout_iq/__init__.py` — current Python model/controller extensions.
- `lunara_checkout_iq/res_config_settings_views.xml` — administrator settings UI.
- `lunara_checkout_iq/checkout_address_views.xml` — checkout form inheritance.
- `lunara_checkout_iq/tests/` — Odoo-side regression tests.
- `docs/ARCHITECTURE.md` — design and boundaries.
- `docs/DEVELOPMENT.md` — test workflow.

## Verification expectations

For documentation-only changes:

- verify Markdown links/paths;
- do not claim runtime testing that did not happen.

For Python/XML changes:

1. run public syntax/static checks;
2. run module-specific Odoo 19 tests in a legitimate disposable test environment when available;
3. report exact commands, exit codes, and failures;
4. update README/CHANGELOG when public behavior changes.

## Review priorities

1. checkout correctness;
2. no regression to standard Odoo behavior;
3. customer-data safety;
4. compatibility with Odoo 19;
5. deterministic phone normalization;
6. clear Arabic/English documentation;
7. maintainability for external contributors.

## Do not overclaim

A passing public GitHub Actions workflow proves only the checks contained in that workflow. It does not prove full Odoo runtime compatibility, production readiness, Odoo certification, or endorsement.
