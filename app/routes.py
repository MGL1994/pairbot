import random

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

        students = [
            cohort_to_pair.student_one,
            cohort_to_pair.student_two,
            cohort_to_pair.student_three,
            cohort_to_pair.student_four,
            cohort_to_pair.student_five,
            cohort_to_pair.student_six,
            cohort_to_pair.student_seven,
            cohort_to_pair.student_eight,
            cohort_to_pair.student_nine,
            cohort_to_pair.student_ten,
            cohort_to_pair.student_eleven,
            cohort_to_pair.student_twelve,
            cohort_to_pair.student_thirteen,
            cohort_to_pair.student_fourteen,
            cohort_to_pair.student_fifteen,
            cohort_to_pair.student_sixteen
        ]

        def randomise_students(ordered_students):
            return random.sample(ordered_students, len(ordered_students))

        def check_for_duplicated_pairs():
            duplicated = True
            duplicated_count = 0
            unique_count = 0
            non_duplicated_students = []
            while duplicated == True:
                randomised_students = randomise_students(students)
                
                pairings_of_cohort = Pairing.query.filter_by(cohort_id=cohort_to_pair.id).all()
                
                existing_pairs = []
                
                for pairs in pairings_of_cohort:
                    existing_pairs.append(pairs.pair_one)
                    existing_pairs.append(pairs.pair_two)
                    existing_pairs.append(pairs.pair_three)
                    existing_pairs.append(pairs.pair_four)
                    existing_pairs.append(pairs.pair_five)
                    existing_pairs.append(pairs.pair_six)
                    existing_pairs.append(pairs.pair_seven)
                    existing_pairs.append(pairs.pair_eight)

                sample_pair_one = randomised_students[0] + ' + ' + randomised_students[1]
                sample_pair_two = randomised_students[1] + ' + ' + randomised_students[0]

                if sample_pair_one in existing_pairs or sample_pair_two in existing_pairs:
                    duplicated_count + 1
                elif unique_count == 15:
                    duplicated_count = False
                    print('END OF PROCESS')
                else:
                    non_duplicated_students = randomised_students
                    duplicated = False
                    unique_count + 1
   
            print('Unique Count:', unique_count)
            print('Duplicated Count:', duplicated_count)
            return non_duplicated_students

        new_pairings = check_for_duplicated_pairs()

        pairing = Pairing(
            pair_one=new_pairings[0] + ' + ' + new_pairings[1],
            pair_two=new_pairings[2] + ' + ' + new_pairings[3],
            pair_three=new_pairings[4] + ' + ' + new_pairings[5],
            pair_four=new_pairings[6] + ' + ' + new_pairings[7],
            pair_five=new_pairings[8] + ' + ' + new_pairings[9],
            pair_six=new_pairings[10] + ' + ' + new_pairings[11],
            pair_seven=new_pairings[12] + ' + ' + new_pairings[13],
            pair_eight=new_pairings[14] + ' + ' + new_pairings[15],
            cohort_id=cohort_to_pair.id
            )
        db.session.add(pairing)
        db.session.commit()
        flash('Check out your pairing')
        return redirect(url_for('cohorts'))
    return render_template('cohort.html', cohort=cohort, form=form, pairings=pairings)