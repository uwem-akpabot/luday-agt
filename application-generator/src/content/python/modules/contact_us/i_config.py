class ContactUsIConfig:

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
	USE_CORS = True
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = os.environ.get('MAIL_PORT')
	MAIL_USE_TLS = as_bool(os.environ.get('MAIL_USE_TLS'))
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAULT_SENDER',
                                       'donotreply@bestdealnaija.com')

 """

 i_config["default"] = default