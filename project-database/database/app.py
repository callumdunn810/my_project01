from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = getenv('DATABASE_URI') 'sqlite:///data.db' 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

########################################################
from my_project import routes


class Countries(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(30), nullable=False)
   cities = db.relationship('Cities', backref='country') 

class Cities(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(30), nullable=False)
   country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

class Users(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   first_name = db.Column(db.String(30), nullable=False)
   last_name = db.Column(db.String(30), nullable=False)


if __name__ == "__main__":
    app.run(debug=True)