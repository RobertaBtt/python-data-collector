import os
from dotenv import load_dotenv
from app.configuration.ConfigurationAbstract import ConfigurationAbstract


class ConfigurationENV(ConfigurationAbstract):
    def __init__(self, config_path: str = '../../.env'):
        self.config = None
        self.path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            config_path
        )

    def load(self) -> None:
        self.config = load_dotenv(dotenv_path=self.path)

    def get(self, key: str, section: str = None):
        if self.config is None:
            self.load()
        return os.environ.get(key)