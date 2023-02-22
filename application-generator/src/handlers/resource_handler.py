from usecase.i_part_handler import IPartHandler
from usecase.i_data_handler import IDataHandler
import sys
from os import path
import logging

logger = logging.getLogger(path.basename(__file__))

class ResourceHandler(IPartHandler):

    def __init__(self, data_handler : IDataHandler):

        self.data_handler = data_handler      

    def handle_part(self, application_name : str, part_information):       
        resource_root_folder = self.data_handler.get_resources_file_path()
        application_root_folder = self.data_handler.get_application_root_folder(application_name)
        
        resource_list = part_information.get("resources")
        for resource in resource_list:
            source = f"{resource_root_folder}/{resource['source']}"
            destination = f"{application_root_folder}/{resource['destination']}"
            logger.debug(f"Attempting to copy resource: {source} -> {destination}")
            self.data_handler.copy_directory(source, destination)             
