import unittest
from app.DependencyContainer import DependencyContainer


class TestServiceSecurity(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.app = DependencyContainer()
        self.service_security = self.app.service_security()

        self.correct_hmac = '9oJnkH8gr3l7UXYlGf3XYEyXKvpf6z0F6w1fJ4aYh5c='

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

    def test_url_webhook_is_registered(self):
        url_webhook_registered = 'djsnckvj'
        self.assertIsNotNone(self.service_security.verify_url_api_key(url_webhook_registered))

    def test_url_webhook_not_registered(self):
        url_webhook_not_registered = 'hello'
        self.assertIsNone(self.service_security.verify_url_api_key(url_webhook_not_registered))

    def test_webhook_signature_is_valid(self):
        url_webhook_registered = 'djsnckvj'
        header_hmac = self.correct_hmac
        self.assertTrue(self.service_security.verify_webhook(url_webhook_registered, self.payload, header_hmac))

    def test_webhook_signature_url_not_found_exception(self):
        url_webhook_registered = 'fake_url'
        header_hmac = self.correct_hmac + "_another_string_added"

        with self.assertRaises(Exception) as context:
            self.service_security.verify_webhook(url_webhook_registered, self.payload, header_hmac)
            self.assertTrue('Webhook Url not found"' in context.exception)

    def test_webhook_signature_is_not_valid_exception(self):
        url_webhook_registered = 'djsnckvj'
        header_hmac = self.correct_hmac + "_another_string_added"

        with self.assertRaises(Exception) as context:
            self.service_security.verify_webhook(url_webhook_registered, self.payload, header_hmac)
            self.assertTrue('Webhook Signature is not valid"' in context.exception)


if __name__ == '__main__':
    unittest.main()

'''curl https://my.webhook.endpoint.com/callback \
  --request POST \
  --header "x-hmac-hash: d12f95e3f98240cff00b2743160455fdf70cb8d431db2981a9af8414fc4ad5f8" \
  --data '{"event":"REFUND_REQUEST","user":"realcustomer@notabaddie.com","amount":"50.25"}'''
