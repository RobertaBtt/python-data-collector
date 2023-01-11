from abc import ABC, abstractmethod


class LogAbstract(ABC):

    @abstractmethod
    def debug(self):
        raise NotImplementedError

    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def warning(self):
        raise NotImplementedError

    @abstractmethod
    def error(self):
        raise NotImplementedError

    @abstractmethod
    def critical(self):
        raise NotImplementedError
