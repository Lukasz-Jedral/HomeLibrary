# app/models.py
from datetime import datetime
from app import db

'''class Authors(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(250), nullable=False)
   last_name = db.Column(db.String(250), index=True, nullable=False)
   description = db.Column(db.String)'''


'''class Publishers(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(250), nullable=False)
   address = db.Column(db.String(250), nullable=False)
   description = db.Column(db.String)'''


class Genres(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50), nullable=False)


class Borrowed(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   last_name= db.Column(db.String(100))
   address = db.Column(db.String(250))
   created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Books(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(250), index=True, nullable=False)
   author = db.Column(db.String(250), index=True, nullable=False)
   genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), index=True, nullable=False)
   description = db.Column(db.String)
   published = db.Column(db.Date)
   publisher = db.Column(db.String(250), index=True, nullable=False)
   cover_url = db.Column(db.String)
   borrowed_id = db.Column(db.Integer)
   #genres = db.relationship("genres", backref="genre", lazy="dynamic")
