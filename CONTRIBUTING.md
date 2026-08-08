# Contributing / المساهمة

Thank you for helping improve Iraq Checkout for Odoo 19.

شكرًا لمساهمتك في تطوير مشروع Iraq Checkout لـ Odoo 19.

## English

### Before opening a pull request

1. Keep the change focused and explain the problem it solves.
2. Keep compatibility with Odoo 19 unless the change explicitly targets a future compatibility branch.
3. Do not include Odoo Enterprise source code, database dumps, customer records, credentials, tokens, private keys, or production logs.
4. Add or update tests when behavior changes.
5. Update documentation when configuration or user-facing behavior changes.
6. Prefer configurable behavior over merchant-specific hardcoding.

### Bug reports

Please include:

- Odoo version/build;
- installed dependencies relevant to the issue;
- exact reproduction steps;
- expected behavior;
- actual behavior;
- a sanitized traceback/log excerpt if applicable.

Never publish secrets or personal customer data in an issue.

### Pull requests

A good PR should contain:

- a clear title;
- a short problem statement;
- a description of the approach;
- testing evidence;
- compatibility notes;
- screenshots for visible checkout/UI changes when useful.

### Coding principles

- Follow normal Odoo model/view/controller extension patterns.
- Avoid monkey-patching when a standard extension point exists.
- Keep normalization and validation deterministic.
- Do not add external network calls without a strong reason and clear documentation.
- Treat phone data as customer data and avoid unnecessary logging.

## العربية

### قبل فتح Pull Request

1. خلي التغيير محدد وواضح واشرح المشكلة التي يحلها.
2. حافظ على توافق Odoo 19 ما لم يكن التغيير مخصصًا لفرع توافق مستقبلي.
3. ممنوع رفع كود Odoo Enterprise أو نسخ قواعد البيانات أو بيانات الزبائن أو كلمات المرور أو Tokens أو Private Keys أو Logs الإنتاج.
4. أضف أو حدّث الاختبارات عند تغيير السلوك.
5. حدّث التوثيق إذا تغيرت الإعدادات أو واجهة المستخدم.
6. الأفضل جعل السلوك قابلًا للتعديل من الإعدادات بدل Hardcode خاص بمتجر واحد.

### بلاغات الأخطاء

أرسل:

- نسخة Odoo;
- الإضافات ذات العلاقة;
- خطوات إعادة المشكلة;
- النتيجة المتوقعة;
- النتيجة الفعلية;
- جزء من الـLog أو Traceback بعد إزالة أي معلومات حساسة.

### المبدأ الأساسي

الهدف أن يبقى المشروع صغيرًا، قابلًا للمراجعة، ومفيدًا لأي مطور أو متجر Odoo يعمل في السوق العراقي، وليس مرتبطًا ببيانات أو أسرار شركة واحدة.
