from usecase.i_data_handler import IDataHandler
import os
import logging
import shutil

logger = logging.getLogger(os.path.basename(__file__))
 
#class PythonSetupHandler(IPythonSetupHandler):  TODO implement parent
class PythonSetupHandler():
    
    def __init__(self, data_handler : IDataHandler):
        self.data_handler = data_handler


    def setup_python_module(self, destination):
        is_path_exist = self.data_handler.is_path_exist(destination)
        if is_path_exist:
            logger.debug(f"Python already setup in {destination}")
        else:
            os.makedirs(destination)
            logger.debug(f"New python module setup in {destination}")    