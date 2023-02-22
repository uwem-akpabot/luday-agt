# app/home/views.py
from . import home_blueprint
from .. import create_app 

app = create_app()

@home_blueprint.route('/', methods=['GET'])
def home():
    return app.send_static_file('index.html')


