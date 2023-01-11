import unittest
from app.DependencyContainer import DependencyContainer


class TestConfigurationENV(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.app = DependencyContainer()
        self.config = self.app.config_env()  # ConfigurationENV

    def test_get_configuration_ENV(self):
        app_name = self.config.get("APP_NAME")
        db_name = self.config.get("DB_NAME")
        self.assertEqual(app_name, "Adaptive Python Service")
        self.assertEqual(db_name, "dbname")


if __name__ == '__main__':
    unittest.main()