# app/__init__.py
import config
import os
from flask import Flask, send_from_directory
from flask_bootstrap import Bootstrap
from flask_cors import CORS

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__, static_folder='../../../build', static_url_path='/')
    CORS(app, support_credentials=True)
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True

    @app.errorhandler(404)
    def not_found(e):
        return app.send_static_file('index.html')

    @app.route('/')
    def index():
        return app.send_static_file('index.html')



    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    bootstrap.init_app(app)

    with app.app_context():
        from .home import home_blueprint
        app.register_blueprint(home_blueprint)

        return app