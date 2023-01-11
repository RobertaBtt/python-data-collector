import unittest
import hashlib
import hmac
import base64


class TestHMACEncryption(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.API_SECRET_KEY = "API_SECRET_CLIENT1"
        self.digest_mode = hashlib.sha256

        self.payload = '''
{
      "event": "SERVER_UPDATE",
      "updates": [
        {
          "item": "gadgets",
          "action": "add",
          "quantity": 20
        },
        {
          "item": "widgets",
          "action": "remove",
          "quantity": 10
        }
      ]
}'''

    def test_hmac_encryption(self):
        # creating a cryptographic hash of the webhook payload
        # This unique signature will be sent in the header

        hmac_result = hmac.new(
            self.API_SECRET_KEY.encode('utf-8'),
            self.payload.encode('utf-8'),
            digestmod=hashlib.sha256)

        hmac_digest = hmac_result.digest()

        computed_mac = base64.b64encode(hmac_digest)
        expected_result = '9oJnkH8gr3l7UXYlGf3XYEyXKvpf6z0F6w1fJ4aYh5c='.encode('utf-8')
        #print(computed_mac)  # 9oJnkH8gr3l7UXYlGf3XYEyXKvpf6z0F6w1fJ4aYh5c=
        result = hmac.compare_digest(computed_mac, expected_result)
        self.assertEqual(computed_mac, expected_result)
        self.assertTrue(result)

    def test_hmac_simple(self):
        simple_payload = '{"event": "SERVER_UPDATE"}'

        hmac_result = hmac.new(
            self.API_SECRET_KEY.encode('utf-8'),
            simple_payload.encode('utf-8'),
            digestmod=hashlib.sha256)

        hmac_digest = hmac_result.digest()

        computed_mac = base64.b64encode(hmac_digest)
        expected_result = 'SgS9OYxlwwM75ttkEJSrMJvVpoXTLrHkWQAJrgFx7LY='.encode('utf-8')

        result = hmac.compare_digest(computed_mac, expected_result)
        self.assertEqual(computed_mac, expected_result)
        self.assertTrue(result)