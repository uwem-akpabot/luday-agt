from abc import ABC, abstractmethod
 
class IPartHandler(ABC):    
    @abstractmethod
    def handle_part(self, application_name : str, Path_information):
        pass