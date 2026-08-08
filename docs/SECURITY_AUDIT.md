# Public repository security audit

**Audit date:** 2026-08-08  
**Repository:** Iraq Checkout for Odoo 19  
**Scope:** public source and documentation created for this repository

## Result

No obvious production credentials or private-key material were identified in the reviewed public project content.

The review checked for common categories of sensitive material, including:

- GitHub access-token signatures;
- Anthropic/API credential signatures;
- generic access-token/client-secret/password assignments;
- RSA/OpenSSH/private-key headers;
- common sensitive file types such as `.env`, private-key files, certificate bundles, database dumps, and production exports.

The module source contains no payment credentials, merchant tokens, customer exports, production database dumps, or Odoo Enterprise source code.

## Repository boundary

This repository is intended to contain only the open-source `lunara_checkout_iq` custom add-on and public project documentation. Production configuration, customer information, server details, proprietary Odoo Enterprise source, and unrelated Lunara modules must remain outside this repository.

## Continuous guardrail

A GitHub Actions security check is included to reject obvious sensitive tracked filenames and several common credential/private-key signatures on pushes and pull requests.

This is a defense-in-depth guardrail, not a guarantee that every possible secret format can be detected. Maintainers should still review changes before merging and rotate/revoke any credential immediately if accidental exposure is ever suspected.

## Contact

Security-sensitive reports should be sent privately to **info@lunara.com.iq**.

Website: https://lunara.com.iq
