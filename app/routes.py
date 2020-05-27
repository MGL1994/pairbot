from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import CohortForm
from app.models import Cohort, Pairing

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = CohortForm()
    if form.validate_on_submit():
        cohort = Cohort(
            cohort_name = form.cohort_name.data,
            student_one = form.student_one.data,
            student_two = form.student_two.data,
            student_three = form.student_three.data,
            student_four = form.student_four.data,
            student_five = form.student_five.data,
            student_six = form.student_six.data,
            student_seven = form.student_seven.data,
            student_eight = form.student_eight.data,
            student_nine = form.student_nine.data,
            student_ten = form.student_ten.data,
            student_eleven = form.student_eleven.data,
            student_twelve = form.student_twelve.data,
            student_thirteen = form.student_thirteen.data,
            student_fourteen = form.student_fourteen.data,
            student_fifteen = form.student_fifteen.data,
            student_sixteen = form.student_sixteen.data
        )
        db.session.add(cohort)
        db.session.commit()
        flash('Register requested for cohort {}'.format(
            form.cohort_name.data))
        return redirect(url_for('cohorts'))
    return render_template('register.html', title='Register', form=form)

@app.route('/cohorts')
def cohorts():
    cohorts = Cohort.query.all()
    pairing = [
        {
            'pairing': cohorts, 
            'pair_one': 'Test', 
            'pair_two': 'Test',
            'pair_three': 'Test',
            'pair_four': 'Test',
            'pair_five': 'Test',
            'pair_six': 'Test',
            'pair_seven': 'Test',
            'pair_eight': 'Test'
        }
    ]
    return render_template('cohorts.html', cohorts=cohorts, pairing=pairing)
    
