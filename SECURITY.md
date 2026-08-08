# Security Policy / سياسة الأمان

## English

### Supported branch

Security fixes currently target the default `main` branch for Odoo 19.

### Reporting a vulnerability

Please do **not** publish exploitable security details, secrets, customer information, database contents, access tokens, private keys, or production credentials in a public issue.

For sensitive reports, use GitHub's private vulnerability reporting/security advisory features when available, or contact the maintainer privately through the contact method listed on the maintainer's GitHub profile.

A useful report includes:

- affected version/commit;
- impact;
- minimal reproduction steps;
- whether the issue requires authentication;
- any safe proof-of-concept details;
- suggested mitigation if known.

### Security boundaries

This module:

- does not require payment gateway credentials;
- does not intentionally make external network calls for its core functionality;
- processes customer contact information already stored by Odoo;
- should not log raw customer phone data unnecessarily;
- does not distribute Odoo Enterprise source code.

### Secret handling

Never commit:

- `.env` files;
- API keys or tokens;
- SSH/private keys;
- database dumps;
- customer exports;
- session files;
- production configuration backups.

## العربية

### الإبلاغ عن ثغرة

لا تنشر تفاصيل ثغرة قابلة للاستغلال أو أي أسرار أو بيانات زبائن أو Tokens أو Private Keys أو بيانات قاعدة الإنتاج داخل Issue عام.

استخدم أدوات GitHub الخاصة بالإبلاغ الأمني الخاص عندما تكون متاحة، أو تواصل مع المسؤول عن المشروع بشكل خاص من خلال معلومات الاتصال الموجودة في حساب GitHub.

### حدود الأمان

الموديول لا يحتاج بيانات بوابة دفع حتى يعمل، ولا يفترض أن ينفذ اتصالات خارجية ضمن وظيفته الأساسية، ولا يحتوي على كود Odoo Enterprise.

### ممنوع رفع

- ملفات `.env`;
- مفاتيح API;
- كلمات المرور;
- Private Keys;
- نسخ قواعد البيانات;
- بيانات الزبائن;
- Logs الإنتاج التي تحتوي معلومات حساسة.
