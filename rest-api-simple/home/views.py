import flask

home_app = flask.Blueprint('home_app', __name__)

@home_app.route('/')
def home():
    return "The API server is running"
