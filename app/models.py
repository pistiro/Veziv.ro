from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    purchased = db.Column(db.Boolean, default=False)