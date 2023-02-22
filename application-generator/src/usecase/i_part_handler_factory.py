from abc import ABC, abstractmethod
import logging
 
class IPartHandlerFactory(ABC):    
    @abstractmethod
    def create_part_handler(self, part_name: str):
        pass