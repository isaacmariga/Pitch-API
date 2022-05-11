from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func
from flask import session



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    password = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)     

    def __repr__(self):
        return f'User {self.username}'


class Pitch (db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_content = db.Column(db.String(200))
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id") )
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')
    votes = db.relationship('Vote', backref='pitch', lazy='dynamic')


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,group_id):
        pitches = Pitch.query.order_by(Pitch.id.desc()).filter_by(group_id=group_id).all()
        return pitches


class Group(db.Model):
  
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='group', lazy='dynamic')

    def save_group(self):
   
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_groups(cls):
        groups = Group.query.all()

        return groups
        
class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment_content = db.Column(db.String)
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id") )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )

    def save_comment(self):
     
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):

        comments = Comment.query.filter_by(pitch_id=pitch_id).all()

        return comments

class Vote(db.Model):
  
    __tablename__ = 'votes'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id") )
    vote_number =  db.Column(db.Integer)

    def save_vote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_votes(cls,user_id,pitch_id):
        votes = Vote.query.filter_by(user_id=user_id, pitch_id=pitch_id).all()
        return votes

    @classmethod
    def num_vote(cls,pitch_id):

        found_votes = db.session.query(func.sum(Vote.vote_number))
        found_votes = found_votes.filter_by(pitch_id=pitch_id).group_by(Vote.pitch_id)
        votes_list = sum([i[0] for i in found_votes.all()])