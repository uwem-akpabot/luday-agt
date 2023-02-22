# app/blogs_api/__init__.py
from flask import Blueprint

blogs_api_blueprint = Blueprint('blogs_api', __name__)

from . import routes