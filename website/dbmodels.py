from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(1000000000), unique=True, nullable=False)
  password = db.Column(db.String(1000000000), nullable=False)
  first_name = db.Column(db.String(1000000000), nullable=False)
  notes = db.relationship('Note')
  

class Note(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  note = db.Column(db.String(1000000),nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  flashcard = db.relationship('Flashcard')

class Flashcard(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  question = db.Column(db.String(1000000),nullable=False)
  answer = db.Column(db.String(1000000),nullable=False)
  incorrect_answer1 = db.Column(db.String(1000000))
  incorrect_answer2 = db.Column(db.String(1000000))
  incorrect_answer3 = db.Column(db.String(1000000))
  note_id= db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
  
  
  
  
  
  