from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CohortForm(FlaskForm):
    cohort_name = StringField('Cohort Name', validators=[DataRequired()])
    student_one = StringField('Student One', validators=[DataRequired()])
    student_two = StringField('Student Two', validators=[DataRequired()])
    student_three = StringField('Student Three', validators=[DataRequired()])
    student_four = StringField('Student Four', validators=[DataRequired()])
    student_five = StringField('Student Five', validators=[DataRequired()])
    student_six = StringField('Student Six', validators=[DataRequired()])
    student_seven = StringField('Student Seven', validators=[DataRequired()])
    student_eight = StringField('Student Eight', validators=[DataRequired()])
    student_nine = StringField('Student Nine', validators=[DataRequired()])
    student_ten = StringField('Student Ten', validators=[DataRequired()])
    student_eleven = StringField('Student Eleven', validators=[DataRequired()])
    student_twelve = StringField('Student Twelve', validators=[DataRequired()])
    student_thirteen = StringField('Student Thirteen', validators=[DataRequired()])
    student_fourteen = StringField('Student Fourteen', validators=[DataRequired()])
    student_fifteen = StringField('Student Fifteen', validators=[DataRequired()])
    student_sixteen = StringField('Student Sixteen', validators=[DataRequired()])
    submit = SubmitField('Register Cohort')