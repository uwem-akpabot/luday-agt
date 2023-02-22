# app/__init__.py
import config
import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS #development ONLY
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from apifairy import APIFairy

db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()
apifairy = APIFairy()
migrate = Migrate(compare_type=True)

def create_app():
    app = Flask(__name__)

    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    if app.config['USE_CORS']:
        CORS(app, support_credentials=True)
        app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    apifairy.init_app(app)

    migrate.init_app(app, db)

    with app.app_context():
        # Register blueprints
        from app.products_api import products_api_blueprint
        app.register_blueprint(products_api_blueprint, url_prefix='/api')
        
        from app.order_api import order_api_blueprint
        app.register_blueprint(order_api_blueprint, url_prefix='/api')

        return app