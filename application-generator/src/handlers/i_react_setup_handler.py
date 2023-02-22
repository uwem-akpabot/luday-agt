from abc import ABC, abstractmethod
 
class IReactSetupHandler(ABC):

    @abstractmethod
    def setup_react_app(self, destination, part_information):
        pass


    @abstractmethod
    def setup_react_package(self, destination):
        pass
