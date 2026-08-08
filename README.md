# Iraq Checkout for Odoo 19

[العربية](#العربية) · [English](#english)

An open-source **Odoo 19.0 compatible** add-on focused on practical e-commerce checkout requirements for Iraqi merchants.

The add-on makes checkout email/phone requirements configurable per website and normalizes common Iraqi phone formats to the international `+964` format, while preserving valid non-Iraqi international numbers.

> **Technical module name:** `lunara_checkout_iq`  
> **Target / Compatibility:** Odoo **19.0**  
> **License:** LGPL-3.0-only  
> **Maintained by:** Lunara Iraq  
> **Website:** https://lunara.com.iq  
> **Contact:** info@lunara.com.iq

---

## English

### Why this project exists

Iraqi e-commerce stores frequently rely on phone-first customer communication and Cash on Delivery workflows. A checkout that always assumes email is the primary identifier can create unnecessary friction. This project provides a small, auditable Odoo 19 extension that lets administrators choose the required checkout fields while handling Iraqi phone numbers consistently.

### Features

- Compatible with **Odoo 19.0** Website/eCommerce checkout.
- Configurable **required or optional email** per website.
- Configurable **required or optional phone** per website.
- Iraqi phone normalization to `+964`.
- Accepts common local input such as `07XX XXX XXXX`.
- Preserves valid non-Iraqi international phone numbers instead of rewriting them as Iraqi numbers.
- Checkout labels reflect whether email/phone are required or optional.
- Multi-website friendly settings through Odoo Website configuration.
- Arabic translation included.
- No external payment API, credentials, or background network dependency is required by this module.

### Compatibility

This repository targets **Odoo 19.0** and the module manifest declares version `19.0.2.1.0`.

Required Odoo modules:

- `website_sale`
- `phone_validation`

The project does not redistribute Odoo Enterprise source code. Users are responsible for using a properly licensed Odoo installation where applicable.

### Installation

1. Copy the `lunara_checkout_iq` directory into an Odoo custom add-ons path.
2. Restart or reload Odoo according to your deployment process.
3. Update the Apps list.
4. Install **Lunara — Checkout: Optional Email & Mandatory Iraqi Phone**.
5. Open Website settings and configure the checkout requirements.

### Configuration

In Website settings, configure:

- **Require email at checkout**
- **Require phone at checkout**

Common Iraqi local numbers such as `07XX XXX XXXX` are normalized to `+964...` when saved.

### Security and privacy

This public repository must never contain:

- API keys, access tokens, passwords, private keys, or `.env` secrets;
- customer names, phone numbers, addresses, orders, or exports;
- production database dumps, logs, hostnames, or private infrastructure details;
- Odoo Enterprise proprietary source code.

Please report security-sensitive issues privately by email to **info@lunara.com.iq** and see [SECURITY.md](SECURITY.md).

### Maintainer

**Lunara Iraq**  
Website: https://lunara.com.iq  
Email: info@lunara.com.iq

---

## العربية

### ما هو المشروع؟

هذا موديول مفتوح المصدر **متوافق مع Odoo 19.0** ومخصص لتحسين تجربة إتمام الطلب للمتاجر الإلكترونية في العراق.

يسمح للمسؤول بتحديد ما إذا كان البريد الإلكتروني أو رقم الهاتف مطلوبًا أو اختياريًا أثناء Checkout، كما يقوم بتوحيد أرقام الهاتف العراقية إلى الصيغة الدولية `+964` مع الحفاظ على أرقام الدول الأخرى.

### المزايا

- متوافق مع **Odoo 19.0** وWebsite/eCommerce.
- جعل البريد الإلكتروني مطلوبًا أو اختياريًا حسب إعداد الموقع.
- جعل رقم الهاتف مطلوبًا أو اختياريًا حسب إعداد الموقع.
- تحويل أرقام العراق إلى صيغة `+964`.
- دعم الصيغة المحلية الشائعة مثل `07XX XXX XXXX`.
- عدم تحويل أرقام الدول الأخرى إلى أرقام عراقية.
- تغيير علامات الحقول في Checkout بحسب كونها مطلوبة أو اختيارية.
- مناسب للـMulti-Website.
- يتضمن ترجمة عربية.
- لا يحتاج هذا الموديول إلى مفاتيح API أو بيانات دفع أو اتصال بخدمة خارجية لكي يعمل.

### التوافق

المشروع يستهدف **Odoo 19.0**، وإصدار الموديول في الـmanifest هو `19.0.2.1.0`.

الموديولات المطلوبة:

- `website_sale`
- `phone_validation`

هذا المستودع لا ينشر كود Odoo Enterprise، ويجب استخدام Odoo وفق الترخيص المناسب.

### التثبيت

1. ضع مجلد `lunara_checkout_iq` داخل مسار Custom Addons في Odoo.
2. أعد تشغيل أو تحميل خدمة Odoo حسب بيئتك.
3. حدّث قائمة Apps.
4. ثبّت موديول **Lunara — Checkout: Optional Email & Mandatory Iraqi Phone**.
5. افتح إعدادات Website وحدد الحقول المطلوبة في Checkout.

### الأمان والخصوصية

يجب ألا يحتوي هذا المستودع العام على أي كلمات مرور أو Tokens أو API Keys أو مفاتيح خاصة أو بيانات زبائن أو Database Dumps أو معلومات البنية التحتية الخاصة أو كود Odoo Enterprise.

للإبلاغ عن مشكلة أمنية بشكل خاص، راسل: **info@lunara.com.iq**.

### الجهة المشرفة

**Lunara Iraq**  
الموقع: https://lunara.com.iq  
البريد الإلكتروني: info@lunara.com.iq

---

## Contributing / المساهمة

Issues and pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md) first.

نرحب بالمساهمات وطلبات الدمج. يرجى قراءة ملفات المساهمة والأمان قبل إرسال أي تغيير.

## License

LGPL-3.0-only. See [LICENSE](LICENSE).
