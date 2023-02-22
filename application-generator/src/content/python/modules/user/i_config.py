class UserIConfig:

 i_config = {}
 
 default = """
import os
from abc import ABC, abstractmethod

def as_bool(value):
    if value:
        return value.lower() in ['true', 'yes', 'on', '1']
    return False

class IConfig(ABC):
	SUPER_ADMIN_EMAIL = os.environ.get('SUPER_ADMIN_EMAIL')
	SUPER_ADMIN_PASSWORD = os.environ.get('SUPER_ADMIN_PASSWORD')
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	BUNDLE_ERRORS = True
	JSON_SORT_KEYS = True # set False on prod
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = os.environ.get('MAIL_PORT')
	MAIL_USE_TLS = as_bool(os.environ.get('MAIL_USE_TLS'))
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAULT_SENDER',
                                       'donotreply@bestdealnaija.com')
	ACCESS_TOKEN_MINUTES = int(os.environ.get('ACCESS_TOKEN_MINUTES') or '45')
	REFRESH_TOKEN_DAYS = int(os.environ.get('REFRESH_TOKEN_DAYS') or '7')
	REFRESH_TOKEN_IN_COOKIE = as_bool(os.environ.get(
        'REFRESH_TOKEN_IN_COOKIE') or 'no')
	REFRESH_TOKEN_IN_BODY = as_bool(os.environ.get('REFRESH_TOKEN_IN_BODY'))
	RESET_TOKEN_MINUTES = int(os.environ.get('RESET_TOKEN_MINUTES') or '15')
	USE_CORS = as_bool(os.environ.get('USE_CORS') or 'yes') # set False on prod
	PASSWORD_RESET_URL = os.environ.get('PASSWORD_RESET_URL') or \
        'http://localhost:3000/reset'
"""
 i_config["default"] = default
