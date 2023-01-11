import unittest
from app.connection.ConnectionSQLite import ConnectionSQLite
from app.DependencyContainer import DependencyContainer
import sqlite3


class TestConnectionSqlite(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.app = DependencyContainer()
        self.config = self.app.config_conf()  # ConfigurationCONF
        self.sql = ConnectionSQLite(self.config, "CONNECTION_SQLITE_TEST")

    def test_get_connection_sqlite3(self):
        connection = self.sql.get_connection()
        self.assertTrue(isinstance(connection, sqlite3.Connection))


if __name__ == '__main__':
    unittest.main()
