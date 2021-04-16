import models
from flask import Response
from app import db
from flask import jsonify
import time

def add_note(note, owner=''):
	if len(note) >= 1:
		new_note = models.Note(id=int(time.time()), note=note, owner=owner)
		try:
			db.session.add(new_note)
			db.session.commit()
			return jsonify(id=new_note.id), 200 # vse ok
		except:
			return Response(status=422) # smth went wrong
	return jsonify(msg="Заметка слишком короткая!"), 401


def get_notes(owner=''):
	try:
		notes = [r.note for r in models.Note.query.filter_by(owner=owner).distinct()] # генерирует список всех заметок
		return jsonify(notes=notes) # переводим в JSON и возвращаем
	except:
		return jsonify(msg="Не найдено ни одной заметки"), 404


def del_note(id):
	try:
		models.Note.query.filter_by(id=id).delete()
		db.session.commit()
		return Response(status=200)
	except:
		return jsonify(msg="Заметка не найдена"), 404