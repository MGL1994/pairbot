import unittest

from app.routes import app
from app.models import Cohort

class BasicTestCase(unittest.TestCase):

    def test_root(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)

class PairsTestCase(unittest.TestCase):

    def setUp(self):
        cohort = Cohort.objects.create(
            cohort_name = 'Test',
            student_one = 'Student One,
            student_two = 'Student Two',
            student_three = 'Student Three',
            student_four = 'Student Four',
            student_five = 'Student Five',
            student_six = 'Student Six',
            student_seven = 'Student Seven',
            student_eight = 'Student Eight',
            student_nine = 'Student Nine',
            student_ten = 'Student Ten',
            student_eleven = 'Student Eleven',
            student_twelve = 'Student Twelve',
            student_thirteen = 'Student Thirteen',
            student_fourteen = 'Student Fourteen',
            student_fifteen = 'Student Fifteen,
            student_sixteen = 'Student Sixteen'
        )

    def test_register(self):
        tester = app.test_client(self)
        response = tester.get('/cohorts', content_type='html/test')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
            unittest.main()