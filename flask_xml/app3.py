import flask
import flask_restful
import simplexml

class MyURL(flask_restful.Resource):
	def get(self):
		return {"dataitem": "data value"}

app = flask.Flask(__name__)
api = flask_restful.Api(app)

#@api.representation('application/xml')
def output_xml(data, code, headers=None):
	resp = flask.make_response(simplexml.dumps({'response' : data}), code)
	resp.headers.extend(headers or {})
	return resp
api.representations['application/xml'] = output_xml

api.add_resource(MyURL, "/")
