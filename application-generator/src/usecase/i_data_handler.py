from abc import ABC, abstractmethod
 
class IDataHandler(ABC):
    
    @abstractmethod
    def write(self, content, path):
        pass

    @abstractmethod
    def copy_file(self, src, dest):
        pass

    @abstractmethod
    def copy_directory(self, src, dest):
        pass

    # Not to be implemented
    def remove(self, file):
        pass
    
    @abstractmethod
    def get_application_root_folder(self, application_name : str):
        pass
    
    @abstractmethod
    def is_path_exist(self, path):
        pass
    
    @abstractmethod
    def get_conf_file_path(self): 
        pass
    
    @abstractmethod
    def get_root_directory(self): 
        pass