class ProductsIConfig:

 i_config = {}

 default = """
import os
from abc import ABC, abstractmethod

def as_bool(value):
    if value:
        return value.lower() in ['true', 'yes', 'on', '1']
    return False
class IConfig(ABC):
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	BUNDLE_ERRORS = True
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = os.environ.get('MAIL_PORT')
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MAIL_USE_TLS = True
	MAIL_USE_SSL = False
	USE_CORS = as_bool(os.environ.get('USE_CORS') or 'yes') # set False on prod
 """

 i_config["default"] = default