import unittest

from app import db, app


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        #app.config['TESTING'] = True
        #app.config['DEBUG'] = True
        self.app = app.test_store()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
