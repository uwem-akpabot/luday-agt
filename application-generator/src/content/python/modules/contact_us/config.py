class ContactUsConfig:

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
    
class DevelopmentConfig(IConfig):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_username}:{db_password}@{db_server}:{db_port}/{db_database}'
    SQLALCHEMY_ECHO = True

class ProductionConfig(IConfig):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_username}:{db_password}@{db_server}:{db_port}/{db_database}'
    SQLALCHEMY_ECHO = False
"""

 config["default"] = default