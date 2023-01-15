import json
from jsonschema import validate
import uuid
from app.serialize.SchemaJSON import schema


class SerializeJSON:

    @staticmethod
    def deserialize_file(str_path_file: str) -> dict:

        try:
            with open(str_path_file) as data_loaded:
                json_data = json.load(data_loaded)
            return json_data
        except FileNotFoundError:
            raise Exception(f'File {str_path_file} not found')

    @staticmethod
    def deserialize_string(content: str) -> dict:

        try:
            # parse JSON from a string
            json_data = json.loads(content)
            return json_data
        except Exception as ex:
            raise ex

    @staticmethod
    def validate_json_file(str_path_file: str) -> bool:
        try:
            json_data = SerializeJSON.deserialize_file(str_path_file)
            result_validation = validate(instance=json_data, schema=schema)

            return result_validation
        except Exception as ex:
            raise ex
        pass

    @staticmethod
    def validate_json_string(content: str) -> bool:
        try:
            json_data = SerializeJSON.deserialize_string(content)
            result_validation = validate(instance=json_data, schema=schema)

            return result_validation
        except Exception as ex:
            raise ex
        pass

    @staticmethod
    def extract_transaction_data(content: dict) -> dict:

        dict_transaction = {}

        job_state = content['job_state']
        has_deliver = content['has_delivery']
        timestamp = None

        if job_state == "Successful" and int(has_deliver) == 1:
            job_id = int(content['job_id'])

            transaction_uuid = str(uuid.uuid4())
            driver_id = None
            driver_name = None

            amount_total = float(content['transaction_fields']['fare_amount'])
            amount_driver = float(content['transaction_fields']['driver_amount'])
            fees_amount = float(content['transaction_fields']['added_fees'])
            timestamp = None
            latitude_start = None
            longitude_start = None
            distance = content['total_distance_travelled']
            time_spent = content['total_time_spent_at_task_till_completion']

            amount_driver += fees_amount
            n_tasks = len(content['task_history'])
            for task in content['task_history']:

                # This is our task - Starts here
                if task['id'] == job_id:

                    # avoid override of these values. We get the first occurrence
                    if timestamp is None:
                        timestamp = task['creation_datetime']
                    if latitude_start is None:
                        latitude_start = task['latitude']
                    if longitude_start is None:
                        longitude_start = task['longitude']
                    if driver_name is None:
                        driver_name = task['fleet_name']
                    if driver_id is None:
                        driver_id = task['fleet_id']

                        break
            latitude_end = content['task_history'][n_tasks - 1]['latitude']
            longitude_end = content['task_history'][n_tasks - 1]['longitude']

            dict_transaction['job_id'] = job_id
            dict_transaction['uuid'] = transaction_uuid
            dict_transaction['timestamp'] = timestamp
            dict_transaction['driver_id'] = driver_id
            dict_transaction['driver_name'] = driver_name
            dict_transaction['amount_total'] = amount_total
            dict_transaction['amount_driver'] = amount_driver
            dict_transaction['distance'] = distance
            dict_transaction['time_spent'] = time_spent
            dict_transaction['amount_currency'] = 'euro'
            dict_transaction['distance_unit'] = 'km'
            dict_transaction['time_spent_unit'] = 'min'
            dict_transaction['original_json'] = content

            return dict_transaction

        else:
            raise Exception(f'This job was not successful ans will not be processed')

