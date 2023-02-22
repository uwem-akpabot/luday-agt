from usecase.i_part_handler_factory import IPartHandlerFactory
from handlers.file_handler import FileHandler
from handlers.react_setup_handler import  ReactSetupHandler
from handlers.python_setup_handler import  PythonSetupHandler

from inspect import getmembers, isclass, isabstract
import usecase
import handlers
from os import path
import logging

logger = logging.getLogger(path.basename(__file__))


class PartHandlerFactory(IPartHandlerFactory):
    part_handlers = {}  # Key = part_name, Value = class for the part_handler

    def __init__(self):
        self.load_part_handlers()

    def load_part_handlers(self):
        classes = getmembers(handlers,
                             lambda handler: isclass(handler) and not isabstract(handler))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, usecase.IPartHandler):
                self.part_handlers.update([[name, _type]])

        logger.debug(f"self.part_handlers  {self.part_handlers}")



    def create_part_handler(self, part_name: str):
        if part_name in self.part_handlers:
            logger.debug(f"Found Part Handler {part_name}")
            if part_name == "ReactHandler":
                return self.part_handlers[part_name](FileHandler(), ReactSetupHandler(FileHandler()))
            elif part_name == "PythonHandler":
                return self.part_handlers[part_name](FileHandler(), PythonSetupHandler(FileHandler()))
            elif part_name == "ResourceHandler":
                return self.part_handlers[part_name](FileHandler())
            elif part_name == "TailwindCssHandler":
                return self.part_handlers[part_name](FileHandler())
            else:
                return self.part_handlers[part_name]()
        else:
            logger.warning(f"No Part Handler available for {part_name}")
            return None
