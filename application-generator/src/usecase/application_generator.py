from usecase.i_part_handler_factory import IPartHandlerFactory
from usecase.i_parser import IParser
from os import path
import logging
 
logger = logging.getLogger(path.basename(__file__))
 
class ApplicationGenerator():
 
    def __init__(self, part_factory: IPartHandlerFactory, parser : IParser):
        self.part_factory = part_factory
        self.parser = parser
   
    def generate_application(self, path_to_configuration_file: str):
        application_setup = self.parser.parse_file(path_to_configuration_file)
        for part in application_setup["parts"]:   
            part_handler = self.part_factory.create_part_handler(part["part_handler"])
            if part_handler is not None:
                part_handler.handle_part(application_setup["application_name"], part)