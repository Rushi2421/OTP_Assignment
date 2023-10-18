import unittest
from OTP_version3 import generate_OTP, validate_mobile, send_otp_over_mobile, validate_email,send_otp


class TestOTPGenerator(unittest.TestCase):
    def test_generate_OTP(self):
        otp = generate_OTP()
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())

    def test_validate_mobile(self):
        self.assertTrue(validate_mobile("1234567890"))
        self.assertFalse(validate_mobile("12345"))
        # Add more test cases for validate_mobile

    def test_send_otp_over_mobile(self):
        result = send_otp_over_mobile("1234567890")
        self.assertTrue(result)

        # You can add more test cases for send_otp_over_mobile

    def test_validate_email(self):
        self.assertTrue(validate_email("example@example.com"))
        self.assertFalse(validate_email("invalid_email"))
        # Add more test cases for validate_email

    def test_send_otp(self):
        result = send_otp("example@example.com")
        self.assertTrue(result)



if __name__ == "__main":
    unittest.main()
