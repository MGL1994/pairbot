from datetime import datetime
from app import db

class Pairing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, unique=True, nullable=False, default=datetime.utcnow)
    pair_one = db.Column(db.String(80), nullable=False)
    pair_two = db.Column(db.String(80), nullable=False)
    pair_three = db.Column(db.String(80), nullable=False)
    pair_four = db.Column(db.String(80), nullable=False)
    pair_five = db.Column(db.String(80), nullable=False)
    pair_six = db.Column(db.String(80), nullable=False)
    pair_seven = db.Column(db.String(80), nullable=False)
    pair_eight = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Date {}>'.format(self.date)