from flask import Response
from flask_jwt_extended import create_access_token
import hashlib
import models
import time
from flask import jsonify
from app import db

def add_user(username, password):
	user = models.User.query.filter_by(username=username).first()
	if user == None:
		user = models.User(id=int(time.time()), username=username.lower(), password=hashlib.md5(password.encode()).hexdigest())
		if len(password) > 6:
			try:
				db.session.add(user)
				db.session.commit()
				return jsonify(msg='Вы успешно зарегистрировались'), 200
			except:
				return jsonify(msg='Ошибка базы данных'), 500
		return jsonify(msg='Пароль слишком короткий'), 401
	return jsonify(msg='Аккаунт с таким именем пользователя уже существует'), 409


def login(username, password):
	user = models.User.query.filter_by(username=username, password=hashlib.md5(password.encode()).hexdigest()).first()
	if user == None:
		return jsonify(msg='Неправильный логин/пароль'), 401
	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token)