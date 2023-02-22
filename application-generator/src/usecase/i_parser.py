from abc import ABC, abstractmethod

class IParser(ABC):
    @abstractmethod
    def parse_file(self, source, dest):
        raise NotImplementedError
