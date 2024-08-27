from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    phone=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150))
    password=db.Column(db.String(150))
    name=db.Column(db.String(150))
    age=db.Column(db.Integer)
    gender=db.Column(db.String(150))
    role=db.Column(db.String(150))
    city=db.Column(db.String(150),nullable=True)
    # meetings = db.relationship('Meetings')
    
# class Meetings(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     user=db.Column(db.Integer,db.ForeignKey('user.phone'))
#     guide = db.Column(db.Integer,db.ForeignKey('user.phone'))
#     link = db.Column(db.String(10000))
    

class Communities(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(150))
    link=db.Column(db.String(10000))
    participants = db.Column(db.Integer)
    
    # members=db.relationship('Members')