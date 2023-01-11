from abc import abstractmethod, ABC


class RepositoryAbstract(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError

    @abstractmethod
    def read(self, query: str):
        raise NotImplementedError

    @abstractmethod
    def read_with_headers(self, query: str):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError

