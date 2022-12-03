from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
db =SQLAlchemy (app)

class User (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email_address = db.Column(db.String(length = 30), nullable=False, unique=30)
    password_hash = db.Column(db.String(length=60), nullable=False)