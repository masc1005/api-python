from src.database.connection import db


class Claims(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
