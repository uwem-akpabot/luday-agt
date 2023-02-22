class HomeConfig:

 config = {}

 default = """ 
import os
from dotenv import load_dotenv
from i_config import IConfig

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class DevelopmentConfig(IConfig):
    ENV = "development"
    DEBUG = True


class ProductionConfig(IConfig):
    ENV = "production"
    DEBUG = False


class TestingConfig(IConfig):
    TESTING = True
"""

 config["default"] = default