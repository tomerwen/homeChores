# test_app.py
import unittest
from main import app, db

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config.from_object('config.TestConfig')
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_database_connection(self):
        response = self.app.get('/chores/Jaanuk')
        self.assertEqual(response.status_code, 200)