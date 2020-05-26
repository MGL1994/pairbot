from flask import render_template, flash, redirect, url_for
from app import app
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
        flash('Register requested for cohort {}'.format(
            form.cohort_name.data))
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)
