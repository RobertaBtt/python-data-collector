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

        self.business_payload = '{"job_latitude":"37.3333333333","fleet_email":"JoehRichmondAndAssociate@example.com","job_id":"236365","job_state":"Successful","has_delivery":"1","job_pickup_latitude":"30.2222222222","job_pickup_name":"JonRichmondPeppy","job_status":"2","sign_image":"https://flolaLux.net","customer_username":"username","job_longitude":"-122.0000000000","job_pickup_longitude":"-122.0000000","total_distance_travelled":"0","total_time_spent_at_task_till_completion":"15","has_pickup":"1","job_token":"304958304958304958","job_pickup_address":"5849GjfoJFOMSMAvenue","job_pickup_phone":"+43574830485","fleet_id":"3635","fleet_name":"Postino","job_pickup_email":"test@email.com","task_history":[{"id":235973,"job_id":85185,"fleet_id":3829,"fleet_name":"bobbysingh","latitude":"30.7192552","longitude":"76.8102558","type":"state_changed","description":"StatusupdatedfromAssignedtoUnassigned","creation_datetime":"2016-01-11T09:34:17.000Z"},{"id":236365,"job_id":85185,"fleet_id":3635,"fleet_name":"PeppyB","latitude":"30.7193512","longitude":"76.8102679","type":"state_changed","description":"Acceptedat","creation_datetime":"2016-01-11T12:11:02.000Z"}],"transaction_fields":{"fare_amount":456.78,"driver_amount":123.45,"added_fees":0}}'

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

    def test_hmac_business(self):
        hmac_result = hmac.new(
            self.API_SECRET_KEY.encode('utf-8'),
            self.business_payload.encode('utf-8'),
            digestmod=hashlib.sha256)

        hmac_digest = hmac_result.digest()

        computed_mac = base64.b64encode(hmac_digest)
        print(computed_mac) # nbulYuM2wST8rtdF39opCYnLoNQozjYgOHiaastNhLs=

        expected_result = 'nbulYuM2wST8rtdF39opCYnLoNQozjYgOHiaastNhLs='.encode('utf-8')

        result = hmac.compare_digest(computed_mac, expected_result)
        self.assertEqual(computed_mac, expected_result)
        self.assertTrue(result)

