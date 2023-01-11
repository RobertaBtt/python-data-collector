import json
from jsonschema import validate
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
