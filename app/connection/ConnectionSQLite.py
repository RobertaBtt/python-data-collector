import sqlite3
from pathlib import Path
import os
from app.connection.ConnectionAbstract import ConnectionAbstract
from app.configuration.ConfigurationAbstract import ConfigurationAbstract

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class ConnectionSQLite(ConnectionAbstract):

    def __init__(self, config: ConfigurationAbstract, section: str):
        self.db_url = config.get(section, "path")

    def get_connection(self) -> ConnectionAbstract:
        try:
            return sqlite3.connect(os.path.join(str(BASE_DIR) + self.db_url))
        except Exception as e:
            raise e

