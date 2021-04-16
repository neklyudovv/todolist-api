import flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "OAnRL$>N*SQ]mboL/:Fg|`P#H!vS#--{'`{P6F|6lG5A]BpOB*oV%W,^TB=x6rx"  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

jwt = JWTManager(app)
db = SQLAlchemy(app)

import notes
import accounts

@app.route('/')
def index(): # возвращает 201, указывая на то, что все работает
	return flask.Response(status=201)


@app.route('/signup', methods = ['POST'])
def sign_up(): # регистрация пользователя
	return accounts.add_user(request.json['username'], request.json['password'])


@app.route('/login', methods = ['POST'])
def sign_in(): # логин пользователя
	return accounts.login(request.json['username'], request.json['password'])


@app.route('/add-note', methods = ['POST'])
def new_note(): # добавление нового таска
	return notes.add_note(request.json['note'])


@app.route('/get-notes', methods = ['GET'])
def get_notes(): # возвращает все таски
	return notes.get_notes()


@app.route('/del-note', methods = ['POST'])
def del_note(): # удаляет таск
	return notes.del_note(request.json['id'])

if __name__ == "__main__":
	app.run(debug=True)