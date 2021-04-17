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

def add_note(note, owner=''):
	if len(note) >= 1:
		if check_user(owner):
			new_note = models.Note(id=int(time.time()), note=note, owner=owner)
			try:
				db.session.add(new_note)
				db.session.commit()
				return jsonify(id=new_note.id), 200 # vse ok
			except:
				return jsonify(msg='Ошибка базы данных'), 500 # smth went wrong
		return jsonify(msg='Пользователь не найден'), 404
	return jsonify(msg='Заметка слишком короткая'), 401


def get_notes(owner=''):
	if check_user(owner):
		try:
			notes = [r.note for r in models.Note.query.filter_by(owner=owner).distinct()] # генерирует список всех заметок
			return jsonify(notes=notes) # переводим в JSON и возвращаем
		except:
			return jsonify(msg='Не найдено ни одной заметки'), 404
	return jsonify(msg='Пользователь не найден'), 404


def del_note(id):
	try:
		models.Note.query.filter_by(id=id).delete()
		db.session.commit()
		return Response(status=200)
	except:
		return jsonify(msg='Заметка не найдена'), 404