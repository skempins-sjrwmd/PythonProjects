import flask
import vendor_data

app = flask.Flask(__name__)

@app.route("/")
def home():
	return "ABSuite"

@app.route("/api/vendors")
def api_allvendors():
	vendor = vendor_data.VendorDB()
	return flask.jsonify({"vendors": vendor.selectVendors() })

@app.route("/api/vendor/<string:vendor_code>")
def api_onevendor(vendor_code):
	vendor = vendor_data.VendorDB()
	return flask.jsonify({"vendors": vendor.selectVendor(vendor_code)})
