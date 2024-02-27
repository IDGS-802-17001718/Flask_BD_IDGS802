from flask_sqlalchemy import SQLAlchemy
import datetime

db=SQLAlchemy()

class Alumnos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apaterno = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)