from app import db
from datetime import date

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    score = db.Column(db.Integer, default=0)
    votes = db.relationship('Vote', backref='user')

class Seminar(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    week = db.Column(db.Integer)
    seminar_date = db.Column(db.DateTime)
    finish = db.Column(db.Integer)
    votes = db.relationship('Vote', backref='seminar')

class Vote(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   seminar_id = db.Column(db.Integer, db.ForeignKey('seminar.id'), nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   minutes_over = db.Column(db.Integer, nullable=False) 
