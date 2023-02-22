class UserConfig:

 config = {}

 default = """ 
import os
from dotenv import load_dotenv
from i_config import IConfig

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

db_server = os.environ['DB_SERVER']
db_port = os.environ['DB_PORT']
db_database = os.environ['DB_DATABASE']
db_username = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
vendor_upload_folder = os.path.join(ROOT_DIR, 'images/vendors')

class DevelopmentConfig(IConfig):
    ENV = "development"
    DEBUG = True
    DISABLE_AUTH = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_username}:{db_password}@{db_server}:{db_port}/{db_database}'


class ProductionConfig(IConfig):
    ENV = "production"
    DEBUG = False
    DISABLE_AUTH = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_username}:{db_password}@{db_server}:{db_port}/{db_database}'


class TestingConfig(IConfig):
    TESTING = True
    DISABLE_AUTH = True

"""

 config["default"] = default