import json
from usecase.i_parser import IParser
from os import path
import logging
 
logger = logging.getLogger(path.basename(__file__))
 
class JSONParser(IParser):
    def parse_file(self, path_to_file : str):
        obj = json.load(open(path_to_file))
        content = None
 
        if not obj:
            raise Exception(f"Parsing of file {path_to_file} was not successfull")
        else:
            try:
                content = obj
                logger.debug(f"Parsing of file {path_to_file} was successfull")
                return content
            except ValueError as e:
                raise e
