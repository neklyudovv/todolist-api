import flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = flask.Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "OAnRL$>N*SQ]mboL/:Fg|`P#H!vS#--{'`{P6F|6lG5A]BpOB*oV%W,^TB=x6rx"  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

jwt = JWTManager(app)
db = SQLAlchemy(app)

import tasks
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


@app.route('/tasks', methods = ['GET'])
@jwt_required()
def get_tasks(): # возвращает все таски конкретного человека, принимает 'username'
	username = get_jwt_identity()
	return tasks.get_tasks(username)


@app.route('/tasks/add', methods = ['POST'])
@jwt_required()
def new_task(): # добавление нового таска, принимает в идеале 'username' и 'text'
				# возвращает айди таска
	username = get_jwt_identity()
	return tasks.add_task(request.json['text'], username)


@app.route('/tasks/del', methods = ['DELETE'])
@jwt_required()
def del_task(): # удаляет таск, принимает айди таска
	username = get_jwt_identity()
	return tasks.del_task(request.json['id'], username)

if __name__ == "__main__":
	app.run(debug=True)