# app/__init__.py
import config
import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS #development ONLY

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_url_path='/', static_folder='../build')
    CORS(app)

    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)
    
    db.init_app(app)

    migrate = Migrate(app, db)

    @app.route("/", defaults={'path':''})
    def serve(path):
        return send_from_directory(app.static_folder,'index.html')

    with app.app_context():
        # Register blueprints
        from .blogs_api import blogs_api_blueprint
        app.register_blueprint(blogs_api_blueprint)
        return app