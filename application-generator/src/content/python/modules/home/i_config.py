class HomeIConfig:

 i_config = {}

 default = """
import os
from abc import ABC, abstractmethod

class IConfig(ABC):
	SECRET_KEY = os.environ.get('SECRET_KEY')
 """

 i_config["default"] = default