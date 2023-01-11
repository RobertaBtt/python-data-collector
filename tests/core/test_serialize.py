import unittest
import json
import os
from pathlib import Path
from app.DependencyContainer import DependencyContainer
from app.serialize.SerializeJSON import SerializeJSON

BASE_DIR = Path(__file__).resolve().parent.parent


class TestSerialize(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.app = DependencyContainer()
        self.config = self.app.config_env()

    def test_get_current_serializer(self):
        current_format = self.config.get("INPUT_FORMAT")
        self.assertEqual(current_format, "JSON")

    def test_instance_serializer(self):
        current_format = self.config.get("INPUT_FORMAT")
        serializer = self.app.serialize_factory()
        self.assertEqual(SerializeJSON, serializer.get_serializer(current_format))
        self.assertEqual(type(serializer.get_serializer(current_format)()), type(SerializeJSON()))

    def test_serialize_json_file(self):
        current_format = self.config.get("INPUT_FORMAT")
        serializer = self.app.serialize_factory().get_serializer(current_format)

        json_file = os.path.join(str(BASE_DIR) + '/storage/test_json.json')
        result = serializer.deserialize_file(json_file)

        self.assertEqual(result['job_id'], '236365')
        self.assertEqual(result['job_pickup_email'], 'test@email.com')
        self.assertEqual("<class 'dict'>", str(type(result)))
        self.assertEqual("<class 'dict'>", str(type(result['transaction_fields'])))

    def test_serialize_json_string(self):
        current_format = self.config.get("INPUT_FORMAT")
        serializer = self.app.serialize_factory().get_serializer(current_format)
        json_string = """
        {
            "job_latitude": "37.3333333333",
            "fleet_email": "JoehRichmondAndAssociate@example.com",
            "job_id": "236365",
            "fleet_id": "3635",
            "fleet_name": "Postino",
            "job_pickup_email": "test@email.com",
            "task_history": [{
                "id": 235973,
                "description": "Status updated from Assigned to Unassigned",
                "creation_datetime": "2016-01-11T09:34:17.000Z"
            }],
            "transaction_fields": {
                "fare_amount": 456.78,
                "driver_amount": 123.45,
                "added_fees": 0
            }
        }
"""
        result = serializer.deserialize_string(json_string)

        self.assertEqual(result['job_id'], '236365')
        self.assertEqual(result['job_pickup_email'], 'test@email.com')
        self.assertEqual("<class 'dict'>", str(type(result)))
        self.assertEqual("<class 'dict'>", str(type(result['transaction_fields'])))


if __name__ == '__main__':
    unittest.main()
