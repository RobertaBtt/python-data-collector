import unittest
from app.DependencyContainer import DependencyContainer


class TestConfigurationCONF(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.app = DependencyContainer()
        self.config = self.app.config_conf()  # ConfigurationCONF

    def test_get_configuration_CONF(self):
        app_name = self.config.get("APP", "name")
        static_path = self.config.get("STORAGE", "path")
        self.assertEqual(app_name, "Adaptive Python Service")
        self.assertEqual(static_path, "storage")


if __name__ == '__main__':
    unittest.main()
