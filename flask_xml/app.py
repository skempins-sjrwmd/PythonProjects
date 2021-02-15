# https://roytuts.com/how-to-return-different-response-formats-json-xml-in-flask-rest-api/
# The default response is JSON
# To return XML, send the HTTP Header: Accept:application/xml

# Install required packages:
# pip install flask
# pip install flask_restful  
# pip install simplexml

import json
from simplexml import dumps
from flask import Flask, make_response
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)
#api = Api(app, default_mediatype='application/xml')
#api = Api(app, default_mediatype='application/json')

@api.representation('application/json')
def output_json(data, code, headers=None):
	resp = make_response(json.dumps({'response' : data}), code)
	resp.headers.extend(headers or {})
	return resp

@api.representation('application/xml')
def output_xml(data, code, headers=None):
	resp = make_response(dumps({'response' : data}), code)
	resp.headers.extend(headers or {})
	return resp

# define the handlers
class Greet(Resource):
	def get(self):
		return {'message' : 'Hello, how are you?'}
	
	def post(self):
		req = request.get_json()
		print('req', req)
		return req, 201

class GreetName(Resource):
	def get(self, name):
		return {'message' : 'Hello ' + name + ', how are you?'}

# map the api resource to the handlers
api.add_resource(Greet, '/')
api.add_resource(GreetName, '/<string:name>')
