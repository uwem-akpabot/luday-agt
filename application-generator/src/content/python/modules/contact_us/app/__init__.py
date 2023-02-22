# app/__init__.py
import config
import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from apifairy import APIFairy
from flask_moment import Moment

db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()
apifairy = APIFairy()
moment = Moment()
migrate = Migrate(compare_type=True)

environment_configuration = os.environ['CONFIGURATION_SETUP']
def create_app(config_class=environment_configuration):
    app = Flask(__name__)

    app.config.from_object(config_class)
    if app.config['USE_CORS']:
        CORS(app, support_credentials=True)
        app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    apifairy.init_app(app)
    moment.init_app(app)

    migrate.init_app(app, db)

    with app.app_context():
        # Register blueprints
        from .contact_api import contact_api_blueprint
        # from .resources.contact import contact_us_api
        app.register_blueprint(contact_api_blueprint)
        # app.register_blueprint(contact_us_api)
        return app