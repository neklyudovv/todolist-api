from flask import Response
from app import db

class User(db.Model): 
	id = db.Column(db.Integer(), primary_key=True, nullable=False)
	username = db.Column(db.String(20), primary_key=True)
	password = db.Column(db.String(), nullable=False)

	def __repr__(self):
		return '<User %r>' % self.username


class Task(db.Model): 
	id = db.Column(db.Integer(), primary_key=True, nullable=False)
	text = db.Column(db.String(300), nullable=False)
	owner = db.Column(db.String(), default='')

	def __repr__(self):
		return '<User %r>' % self.id

db.create_all()