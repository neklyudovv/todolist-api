import flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import notes
import accounts

@app.route('/')
def index(): # возвращает 201, указывая на то, что все работает
	return flask.Response(status=201)


#@app.route('/signup', methods = ['GET', 'POST'])
#def sign_up():
#	if request.method == 'POST': # регистрирует юзера
#		return accounts.add_user(request.json['username'], request.json['password'])
#	return flask.Response(status=400)


#@app.route('/login', methods = ['GET', 'POST'])
#def sign_in():
#	if request.method == 'POST': # авторизовывает юзера
#		return accounts.login(request.json['username'], request.json['password'])
#	return flask.Response(status=400)


@app.route('/add-note', methods = ['GET', 'POST'])
def new_note():
	if request.method == 'POST': # добавляет заметку данному юзеру
		return notes.add_note(request.json['note'])
	return flask.Response(status=400)


@app.route('/get-notes', methods = ['GET', 'POST'])
def get_notes():
	if request.method == 'GET': #  возвращает все заметки от данного юзера
		return notes.get_notes()
	return flask.Response(status=400)


@app.route('/del-note', methods = ['GET', 'POST'])
def del_note():
	if request.method == 'POST':
		return notes.del_note(request.json['id'])
	return flask.Response(status=400)

if __name__ == "__main__":
	app.run(debug=True)