from odoo.tests.common import TransactionCase


class TestIraqPhoneNormalization(TransactionCase):
    def setUp(self):
        super().setUp()
        self.Partner = self.env["res.partner"]

    def test_local_mobile_is_normalized_to_964(self):
        self.assertEqual(
            self.Partner._lunara_normalize_iq_number("0770 123 4567"),
            "+9647701234567",
        )

    def test_00964_format_is_normalized(self):
        self.assertEqual(
            self.Partner._lunara_normalize_iq_number("00964 770 123 4567"),
            "+9647701234567",
        )

    def test_existing_964_format_is_preserved(self):
        self.assertEqual(
            self.Partner._lunara_normalize_iq_number("+9647701234567"),
            "+9647701234567",
        )

    def test_foreign_international_number_is_preserved(self):
        self.assertEqual(
            self.Partner._lunara_normalize_iq_number("+49 170 1234567"),
            "+491701234567",
        )

    def test_short_unrecognized_value_is_not_rewritten(self):
        self.assertEqual(
            self.Partner._lunara_normalize_iq_number("0770"),
            "0770",
        )

    def test_partner_create_applies_normalization(self):
        partner = self.Partner.create(
            {
                "name": "Checkout Test Partner",
                "phone": "0770 123 4567",
            }
        )
        self.assertEqual(partner.phone, "+9647701234567")
