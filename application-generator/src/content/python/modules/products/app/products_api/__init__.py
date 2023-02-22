# app/products_api/__init__.py
from flask import Blueprint

products_api_blueprint = Blueprint('products_api', __name__)

from . import routes