from app.log.LogAbstract import LogAbstract
from app.configuration.ConfigurationAbstract import ConfigurationAbstract

import logging


class LogLocal(LogAbstract):

    def __init__(self, config: ConfigurationAbstract):
        self.config = config

        self.local_file_name = self.config.get('LOG_FILE')

        self.local_file_mode = 'a'
        self.local_level = self.get_level()
        self.local_format = self.config.get('LOG_FORMAT') #'[%(asctime)s] %(name)s.%(levelname)s %(message)s'
        self.date_format = self.config.get('LOG_DATE_FORMAT') # '%Y-%m-%d %H:%M:%S'

        logging.basicConfig(
            format=self.local_format,
            level=self.local_level,
            datefmt=self.date_format,
            filename=self.local_file_name,
            filemode=self.local_file_mode
        )

        self.logger = logging.getLogger("Log Local")

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.critical(message)

    def get_name(self) -> str:
        return self.config.get('LOG_NAME')

    def get_level(self) -> int:
        return getattr(logging, self.config.get('LOG_LEVEL'))

