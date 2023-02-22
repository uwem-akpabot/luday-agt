# app/schemas.py
from flask import current_app	
from marshmallow import validate, validates, \
    ValidationError
from app import ma, db
from app.models import ContactUsModel


class EmptySchema(ma.Schema):
    pass

class CustomMailSchema(ma.Schema):
    to = ma.String(required=True)
    subject = ma.String(required=True)
    template = ma.String(required=True)
    kwargs = ma.Mapping(ma.String, ma.String)