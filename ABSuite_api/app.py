import flask
import vendor_data

app = flask.Flask(__name__)

@app.route("/")
def home():
	return "ABSuite"

@app.route("/api/vendors")
def api_vendors():
	return flask.jsonify(vendor_data.db)
