from datetime import datetime
from app import db

class Cohort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cohort_name = db.Column(db.String(80), index=True, unique=True, nullable=False)
    student_one = db.Column(db.String(80), nullable=False)
    student_two = db.Column(db.String(80), nullable=False)
    student_three = db.Column(db.String(80), nullable=False)
    student_four = db.Column(db.String(80), nullable=False)
    student_five = db.Column(db.String(80), nullable=False)
    student_six = db.Column(db.String(80), nullable=False)
    student_seven = db.Column(db.String(80), nullable=False)
    student_eight = db.Column(db.String(80), nullable=False)
    student_nine = db.Column(db.String(80), nullable=False)
    student_ten = db.Column(db.String(80), nullable=False)
    student_eleven = db.Column(db.String(80), nullable=False)
    student_twelve = db.Column(db.String(80), nullable=False)
    student_thirteen = db.Column(db.String(80), nullable=False)
    student_fourteen = db.Column(db.String(80), nullable=False)
    student_fifteen = db.Column(db.String(80), nullable=False)
    student_sixteen = db.Column(db.String(80), nullable=False)
    pairings = db.relationship('Pairing', backref='pairing', lazy='dynamic')

    def __repr__(self):
        return '<Cohort {}>'.format(self.cohort_name)

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
    pairing_id = db.Column(db.Integer, db.ForeignKey('cohort.id'))

    def __repr__(self):
        return '<Date {}>'.format(self.date)