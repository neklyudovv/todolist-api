import models
from flask import Response
from app import db
from flask import jsonify
import models
import time

def check_user(username):
	user = models.User.query.filter_by(username=username).first()
	if user == None and username != '':
		return False
	return True

def add_task(text, owner=''):
	if len(text) >= 1:
		if check_user(owner):
			new_task = models.Task(id=int(time.time()), text=text, owner=owner)
			try:
				db.session.add(new_task)
				db.session.commit()
				return jsonify(id=new_task.id, text=text, owner=owner), 200
			except:
				return jsonify(msg='Ошибка базы данных'), 500
		return jsonify(msg='Пользователь не найден'), 404
	return jsonify(msg='Текст задачи слишком короткий'), 401


def get_tasks(owner=''):
	if check_user(owner):
		try:
			tasks = [{"id" : item.id, "text" : item.text, "owner" : item.owner} for item in models.Task.query.filter_by(owner=owner).distinct()] # генерирует список всех заметок
			return jsonify(tasks)
		except:
			return jsonify(tasks=[])
	return jsonify(msg='Пользователь не найден'), 404


def del_task(id, owner=''):
	if models.Task.query.filter_by(id=id, owner=owner).first() == None:
		return jsonify(msg='Задача не найдена'), 404
	
	models.Task.query.filter_by(id=id).delete()
	db.session.commit()
	return jsonify(id=id)