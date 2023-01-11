import unittest
import os
from pathlib import Path
from app.DependencyContainer import DependencyContainer
from app.serialize.SerializeJSON import SerializeJSON
from jsonschema.exceptions import ValidationError

BASE_DIR = Path(__file__).resolve().parent.parent

valid_json_string = """
{
  "job_latitude":"37.3333333333",
  "fleet_email":"JoehRichmondAndAssociate@example.com",
  "job_id":"236365",
  "job_state":"Successful",
  "has_delivery":"1",
  "job_pickup_latitude":"30.2222222222",
  "job_pickup_name":"Jon Richmond Peppy",
  "job_status":"2",
  "sign_image":"https://flolaLux.net",
  "customer_username":"username",
  "job_longitude":"-122.0000000000",
  "job_pickup_longitude":"-122.0000000",
  "total_distance_travelled":"0",
  "total_time_spent_at_task_till_completion":"15",
  "has_pickup":"1",
  "job_token":"304958304958304958",
  "job_pickup_address":"5849 Gjfo JFOMSM Avenue",
  "job_pickup_phone":"+43574830485",
  "fleet_id":"3635",
  "fleet_name":"Postino",
  "job_pickup_email":"test@email.com",
  "task_history":[
    {
      "id":235973,
      "job_id":85185,
      "fleet_id":3829,
      "fleet_name":"bobby singh",
      "latitude":"30.7192552",
      "longitude":"76.8102558",
      "type":"state_changed",
      "description":"Status updated from Assigned to Unassigned",
      "creation_datetime":"2016-01-11T09:34:17.000Z"
    },
    {
      "id":236365,
      "job_id":85185,
      "fleet_id":3635,
      "fleet_name":"Peppy B",
      "latitude":"30.7193512",
      "longitude":"76.8102679",
      "type":"state_changed",
      "description":"Accepted at",
      "creation_datetime":"2016-01-11T12:11:02.000Z"
    }
  ],
  "transaction_fields": {
    "fare_amount": 456.78,
    "driver_amount": 123.45,
    "added_fees": 0
  }
}

"""

not_valid_json_string = """
{
  "job_latitude":"37.3333333333",
  "fleet_email":"JoehRichmondAndAssociate@example.com",
  "job_id":"236365",
   "fleet_id":"3635",
  "fleet_name":"Postino",
  "job_pickup_email":"test@email.com",
  "task_history":[
    {
      "id":235973,
      "job_id":85185,
      "fleet_id":3829,
      "fleet_name":"bobby singh",
      "latitude":"30.7192552",
      "longitude":"76.8102558",
      "type":"state_changed",
      "description":"Status updated from Assigned to Unassigned",
      "creation_datetime":"2016-01-11T09:34:17.000Z"
    },
    {
      "id":236365,
      "job_id":85185,
      "fleet_id":3635,
      "fleet_name":"Peppy B",
      "latitude":"30.7193512",
      "longitude":"76.8102679",
      "type":"state_changed",
      "description":"Accepted at",
      "creation_datetime":"2016-01-11T12:11:02.000Z"
    }
  ],
  "transaction_fields": {
    "fare_amount": 456.78,
    "driver_amount": 123.45,
    "added_fees": 0
  }
}

"""


class TestSerialize(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.app = DependencyContainer()
        self.config = self.app.config_env()
        self.current_format = self.config.get("INPUT_FORMAT")
        self.serializer = self.app.serialize_factory().get_serializer(self.current_format)

    def test_get_current_serializer(self):
        current_format = self.config.get("INPUT_FORMAT")
        self.assertEqual(current_format, "JSON")

    def test_instance_serializer(self):

        serializer = self.app.serialize_factory()
        self.assertEqual(SerializeJSON, serializer.get_serializer(self.current_format))
        self.assertEqual(type(serializer.get_serializer(self.current_format)()), type(SerializeJSON()))

    def test_serialize_json_file(self):

        json_file = os.path.join(str(BASE_DIR) + '/storage/test_json.json')
        result = self.serializer.deserialize_file(json_file)

        self.assertEqual(result['job_id'], '236365')
        self.assertEqual(result['job_pickup_email'], 'test@email.com')
        self.assertEqual("<class 'dict'>", str(type(result)))
        self.assertEqual("<class 'dict'>", str(type(result['transaction_fields'])))

    def test_serialize_json_string(self):
        current_format = self.config.get("INPUT_FORMAT")
        serializer = self.app.serialize_factory().get_serializer(current_format)

        result = serializer.deserialize_string(valid_json_string)

        self.assertEqual(result['job_id'], '236365')
        self.assertEqual(result['job_pickup_email'], 'test@email.com')
        self.assertEqual("<class 'dict'>", str(type(result)))
        self.assertEqual("<class 'dict'>", str(type(result['transaction_fields'])))

    def test_json_schema_valid_from_file(self):
        json_file = os.path.join(str(BASE_DIR) + '/storage/test_json.json')
        try:
            self.serializer.validate_json_file(json_file)
        # Schema is ok, no exception raised
        except Exception as exc:
            assert False, f"'{exc}"

    def test_json_schema_not_valid_from_file(self):
        json_file = os.path.join(str(BASE_DIR) + '/storage/test_wrong_json.json')

        try:
            self.serializer.validate_json_file(json_file)
        except Exception as exc:
            assert True, exc

    def test_json_schema_valid_from_string(self):

        try:
            self.serializer.validate_json_string(valid_json_string)
        except Exception as exc:
            assert False, f"'{exc}"

    def test_json_schema_not_valid_from_string(self):

        try:
            self.serializer.validate_json_string(not_valid_json_string)
        except Exception as exc:
            assert True, exc


if __name__ == '__main__':
    unittest.main()
