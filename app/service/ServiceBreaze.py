from pathlib import Path
import os
from app.repository.RepositoryAbstract import RepositoryAbstract
from app.configuration.ConfigurationAbstract import ConfigurationAbstract

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def __query_from_file__(file_query, parameter_id=''):
    with open(file_query, 'r') as query:
        sql_script = query.read() + (str(parameter_id))
    return sql_script


class ServiceBreaze:

    def __init__(self, config: ConfigurationAbstract, repository: RepositoryAbstract):
        self.repository = repository
        self.static_folder = config.get("STORAGE", "path")

    def save_transaction(self, dictionary_data: dict):
        file_path_create_table = "create_table.sql"
        file_query = os.path.join(BASE_DIR, self.static_folder, file_path_create_table)

        query = __query_from_file__(file_query)

        # Creates table if not exists
        try:
            self.repository.create(query)
        except Exception as ex:
            raise ex

        job_id = dictionary_data['job_id']
        uuid = dictionary_data['uuid']
        timestamp = dictionary_data['timestamp']
        driver_id = dictionary_data['driver_id']
        driver_name = dictionary_data['driver_name']
        amount_total = dictionary_data['amount_total']
        amount_driver = dictionary_data['amount_driver']
        distance = dictionary_data['distance']
        time_spent = dictionary_data['time_spent']
        amount_currency = dictionary_data['amount_currency']
        distance_unit = dictionary_data['distance_unit']
        time_spent_unit = dictionary_data['time_spent_unit']
        original_json = dictionary_data['original_json']

        query = f"INSERT INTO transactions (job_id, uuid, timestamp ,driver_id, driver_name, amount_total, amount_driver, distance, time_spent, amount_currency, distance_unit, time_spent_unit,original_json)" \
                f" VALUES( '{job_id}','{uuid}', '{timestamp}', {driver_id},  '{driver_name}' , " \
                f"{amount_total}, {amount_driver}, '{distance}', '{time_spent}', '{amount_currency}', '{distance_unit}', '{time_spent_unit}', \"{original_json}\");"

        try:
            self.repository.create(query)
        except Exception as ex:
            raise ex

