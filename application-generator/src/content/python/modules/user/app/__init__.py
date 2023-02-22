# app/__init__.py
import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_cors import CORS 
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

    seeder = FlaskSeeder()
    seeder.init_app(app, db)
    migrate.init_app(app, db)


    with app.app_context():
        # Register blueprints
        from app.auth_api import auth_api_blueprint
        app.register_blueprint(auth_api_blueprint, url_prefix='/api')
        from app.auth_api import tokens_api_blueprint
        app.register_blueprint(tokens_api_blueprint, url_prefix='/api')

        from app.user_api import user_api_blueprint
        app.register_blueprint(user_api_blueprint, url_prefix='/api')
        return app