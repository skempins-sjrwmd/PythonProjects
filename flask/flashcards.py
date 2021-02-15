#from flask import Flask, render_template
import flask as flask
import model as model
import datetime

app = flask.Flask(__name__)

@app.route("/")
def welcome():
	return flask.render_template("welcome.html", cards=model.db)

@app.route("/card/<int:index>")
def view_card(index):
	try:
		card = model.db[index]
		return flask.render_template("card.html", card=card, index=index, max_index=len(model.db)-1)
	except IndexError:
		flask.abort(404)

@app.route("/api/card")
def api_card_list():
	return flask.jsonify(model.db)
	
@app.route("/api/card/<int:index>")
def api_card_detail(index):
	try:
		return model.db[index]
	except IndexError:
		flask.abort(404)