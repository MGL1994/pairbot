from app import app, db
from app.models import Cohort, Pairing

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Cohort': Cohort, 'Pairing': Pairing}