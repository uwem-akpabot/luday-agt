from usecase.part_handler_factory import PartHandlerFactory
from usecase.application_generator import ApplicationGenerator
from usecase.json_parser import JSONParser
from handlers.file_handler import FileHandler
import argparse
import logging
import sys

def setup_argparse():
    parser = argparse.ArgumentParser(description='Generate Web or Mobile Application')
    parser.add_argument('--conf', metavar='<FILE_NAME>', required=True,
                        help='FILE_NAME. A json file under ../src/main')
    return parser.parse_args()

      
if __name__ == "__main__":
    logging.basicConfig(format='%(name)s - %(levelname)s: %(message)s', level=logging.DEBUG)
    
    sys.path.append(FileHandler.get_root_directory)
    config_file = setup_argparse().conf
    
    part_factory = PartHandlerFactory()
    json_parser = JSONParser()
    application_generator = ApplicationGenerator(part_factory, json_parser)
    
    path_to_application_configuration = f"{FileHandler().get_conf_file_path()}/{config_file}"
    
    application_generator.generate_application(path_to_application_configuration) 