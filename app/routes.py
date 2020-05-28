from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import CohortForm, GeneratePairsForm
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
    return render_template('cohorts.html', cohorts=cohorts)
    
@app.route('/cohort/<cohort_name>', methods=['GET', 'POST'])
def cohort(cohort_name):
    cohort = Cohort.query.filter_by(cohort_name=cohort_name).first_or_404()
    pairings = Pairing.query.filter_by(cohort_id=cohort.id)
    form = GeneratePairsForm()
    if form.validate_on_submit():
        cohort_to_pair_name = form.cohort_name.data
        cohort_to_pair = Cohort.query.filter_by(cohort_name=cohort_to_pair_name).first()
        pairing = Pairing(
            pair_one=cohort_to_pair.student_one + ' and ' + cohort_to_pair.student_two,
            pair_two=cohort_to_pair.student_three + ' and ' + cohort_to_pair.student_four,
            pair_three=cohort_to_pair.student_five + ' and ' + cohort_to_pair.student_six,
            pair_four=cohort_to_pair.student_seven + ' and ' + cohort_to_pair.student_eight,
            pair_five=cohort_to_pair.student_nine + ' and ' + cohort_to_pair.student_ten,
            pair_six=cohort_to_pair.student_eleven + ' and ' + cohort_to_pair.student_twelve,
            pair_seven=cohort_to_pair.student_thirteen + ' and ' + cohort_to_pair.student_fourteen,
            pair_eight=cohort_to_pair.student_fifteen + ' and ' + cohort.student_sixteen,
            cohort_id=cohort_to_pair.id
            )
        db.session.add(pairing)
        db.session.commit()
        flash('Check out your pairing')
        return redirect(url_for('cohorts'))
    return render_template('cohort.html', cohort=cohort, form=form, pairings=pairings)