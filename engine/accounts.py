from flask import Response
import hashlib
import models
from app import db

def add_user(username, password):
	user = models.User(id=int(time.time()), username=username.lower(), password=hashlib.md5(password.encode()).hexdigest())
	if len(password) > 6:
		try:
			db.session.add(user)
			db.session.commit()
			return 'Вы успешно зарегистрировались', 200
		except:
			return 'Аккаунт с таким именем пользователя уже существует', 401
	return 'Пароль слишком короткий', 401


def login(username, password):
	try:
		user = models.User.query.filter_by(username=username, password=hashlib.md5(password.encode()).hexdigest()).first()	
		# jwt token
	except:
		return 'Проверьте правильность введенных данных', 401