# app/contact_api/__init__.py
from flask import Blueprint

contact_api_blueprint = Blueprint('contact_api', __name__)

from . import routes