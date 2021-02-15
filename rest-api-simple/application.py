import flask
from home.views import home_app
from pet.views import pet_app
#from app.views import app_app

def create_app(**config_overrides):
    app = flask.Flask(__name__)

    # load external config file
    app.config.from_pyfile('settings.py')

    # apply overrides for tests
    app.config.update(config_overrides)

    # register blueprints
    app.register_blueprint(home_app)
    app.register_blueprint(pet_app)
#    app.register_blueprint(app_app)

    return app
