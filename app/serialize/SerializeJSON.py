import json


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
            json_data = json.loads(content)
            return json_data
        except Exception as ex:
            raise ex

    @staticmethod
    def from_str_to_list(input_str):
        return input_str.strip('][').replace("'", "").split(', ')
