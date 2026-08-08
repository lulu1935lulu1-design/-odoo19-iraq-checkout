# Iraq Checkout for Odoo 19

[العربية](#العربية) · [English](#english)

An open-source Odoo 19 add-on focused on practical e-commerce checkout requirements for Iraqi merchants.

The add-on makes checkout email/phone requirements configurable per website and normalizes common Iraqi phone formats to the international `+964` format, while preserving valid non-Iraqi international numbers.

> **Technical module name:** `lunara_checkout_iq`  
> **Target version:** Odoo 19.0  
> **License:** LGPL-3.0-only

---

## English

### Why this project exists

Iraqi e-commerce stores frequently rely on phone-first customer communication and Cash on Delivery workflows. A checkout that always assumes email is the primary identifier can create unnecessary friction. This project provides a small, auditable Odoo 19 extension that lets administrators choose the required checkout fields while handling Iraqi phone numbers consistently.

### Features

- Odoo 19 Website/eCommerce checkout integration.
- Configurable **required or optional email** per website.
- Configurable **required or optional phone** per website.
- Iraqi phone normalization to `+964`.
- Accepts common local input such as `07XX XXX XXXX`.
- Preserves valid non-Iraqi international phone numbers instead of rewriting them as Iraqi numbers.
- Checkout labels reflect whether email/phone are required or optional.
- Multi-website friendly settings through Odoo Website configuration.
- No payment credentials, customer exports, database dumps, or production secrets are required by this module.
- No external API or background network call is required for the core functionality.

### Compatibility

| Component | Status |
|---|---|
| Odoo | 19.0 |
| `website_sale` | Required |
| `phone_validation` | Required |
| Odoo Community | Uses standard add-on APIs where dependencies are available |
| Odoo Enterprise | Compatible as a custom add-on; **Enterprise source code is not distributed here** |

Other Odoo versions have not been validated by this repository.

### Installation

1. Clone or download this repository.
2. Copy the `lunara_checkout_iq` directory into one of your Odoo custom add-ons paths.
3. Restart/reload Odoo according to your deployment process.
4. Update the Apps list.
5. Install **Iraq Checkout for Odoo 19** / the technical module `lunara_checkout_iq`.

Example:

```bash
git clone https://github.com/lulu1935lulu1-design/-odoo19-iraq-checkout.git
```

Then add the repository/module directory to your Odoo add-ons path using the normal method for your deployment.

### Configuration

Open Odoo Website settings and configure:

- **Require email at checkout**
- **Require phone at checkout**

Typical Iraqi mobile input:

```text
0770 123 4567
```

is normalized to:

```text
+9647701234567
```

### Design principles

This project intentionally stays small and reviewable:

- use Odoo's existing website and partner models instead of creating a parallel checkout engine;
- do not store credentials or secrets;
- keep checkout policy configurable instead of hardcoding one merchant's workflow;
- normalize phone data in one consistent format for downstream operations;
- keep proprietary Odoo Enterprise source code outside this repository.

### Security and privacy

Never commit `.env` files, access tokens, private keys, database backups, customer exports, production logs, or other secrets. See [SECURITY.md](SECURITY.md).

### Testing

The repository includes lightweight public CI checks that do not require proprietary Odoo source code, plus Odoo-side tests that can be run in a legitimate Odoo 19 environment.

A green public CI badge only proves the checks defined in this repository; it does **not** claim certification by Odoo or full production validation.

### Contributing

Issues and pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

Useful contributions include:

- tests for Iraqi phone formats;
- Odoo 19 compatibility improvements;
- Arabic translations and documentation;
- checkout accessibility improvements;
- reproducible bug reports;
- support for additional Iraqi e-commerce conventions without merchant-specific hardcoding.

### Roadmap

See [ROADMAP.md](ROADMAP.md). The project prioritizes reliability, tests, documentation, and reusable Iraq-focused checkout behavior over merchant-specific features.

### Scope and legal note

This repository contains original/custom add-on code only. It does **not** include or grant rights to Odoo Enterprise source code, databases, customer data, payment credentials, or third-party proprietary software.

Odoo is a trademark of Odoo S.A. This community project is not an official Odoo product and is not endorsed by Odoo S.A.

### License

LGPL-3.0-only. See [LICENSE](LICENSE).

---

## العربية

### ما هو المشروع؟

هذا موديول مفتوح المصدر لـ **Odoo 19** يركز على احتياجات الـCheckout للمتاجر الإلكترونية في العراق، خصوصًا المتاجر التي تعتمد على رقم الهاتف والتواصل المباشر والدفع عند الاستلام.

يتيح الموديول لمسؤول الموقع تحديد ما إذا كان البريد الإلكتروني أو رقم الهاتف **إلزاميًا أو اختياريًا** أثناء إتمام الطلب، ويقوم بتوحيد أرقام الهاتف العراقية إلى الصيغة الدولية `+964`.

### أهم المميزات

- متوافق مع Checkout في Odoo 19.
- جعل البريد الإلكتروني مطلوبًا أو اختياريًا من إعدادات الموقع.
- جعل رقم الهاتف مطلوبًا أو اختياريًا من إعدادات الموقع.
- تحويل صيغ الأرقام العراقية الشائعة إلى `+964`.
- قبول الإدخال المحلي مثل `07XX XXX XXXX`.
- عدم تحويل الأرقام الدولية الصحيحة غير العراقية إلى رقم عراقي.
- تحديث شكل الحقول ليعكس إذا كانت مطلوبة أو اختيارية.
- دعم إعدادات مستقلة لكل Website.
- لا يحتاج الموديول إلى مفاتيح دفع أو Tokens أو بيانات زبائن حتى يعمل.
- الوظيفة الأساسية لا تحتاج اتصالًا بخدمة خارجية.

### المتطلبات

- Odoo 19.0
- `website_sale`
- `phone_validation`

### التثبيت

1. نزّل أو استنسخ المستودع.
2. ضع مجلد `lunara_checkout_iq` داخل مسار الـCustom Addons في Odoo.
3. أعد تحميل/تشغيل Odoo حسب طريقة تشغيل سيرفرك.
4. حدّث قائمة Apps.
5. ثبّت الموديول `lunara_checkout_iq`.

### الإعداد

من إعدادات Website يمكنك التحكم في:

- **Require email at checkout** — هل البريد الإلكتروني إلزامي؟
- **Require phone at checkout** — هل رقم الهاتف إلزامي؟

مثال:

```text
0770 123 4567
```

يصبح:

```text
+9647701234567
```

### الأمان والخصوصية

لا ترفع إلى GitHub ملفات `.env` أو كلمات المرور أو Tokens أو Private Keys أو نسخ قواعد البيانات أو بيانات الزبائن أو سجلات الإنتاج. راجع [SECURITY.md](SECURITY.md).

### المساهمة

المساهمات مرحب بها، خصوصًا الاختبارات، تحسين توافق Odoo 19، التوثيق والترجمة العربية، وتحسين تجربة Checkout للسوق العراقي. راجع [CONTRIBUTING.md](CONTRIBUTING.md).

### الترخيص

المشروع منشور بترخيص **LGPL-3.0-only**. هذا المستودع لا يحتوي على كود Odoo Enterprise ولا يمنح أي حق في البرامج المملوكة لطرف ثالث.
