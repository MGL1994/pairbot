from flask import render_template
from app import app
from app.models import Cohort, Pairing

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
