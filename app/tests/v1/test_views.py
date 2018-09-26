"""Docstring for test_views"""
# system imports
import os
import sys

base_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(base_dir)

# third party module imports
import unittest

# local imports
from app.api import create_app
from app.api.v1.models import Orders


class TestViews(unittest.TestCase):
    """Docstring for Test_views class"""

    def setUp(self):
        """set up the tests and the app"""

        self.app = create_app(config_filename='testing')
        self.client = self.app.test_client
        self.email = 'mufasa@email.com'
        self.password = 'mfs@18'
        self.food = 'burger'
        self.cost = 200

    def test_signup(self):
        """Test user registration"""
        response = self.client().post('/api/v1/signup', data={'email': self.email,
                                                              'pass': self.password})
        self.assertEqual(response.status_code, 201)

    def test_placeorder_without_loggin(self):
        """Check if the request is possible if not logged on"""
        response = self.client().post('/api/v1/', data={"food": self.food,
                                                        "cost": self.cost})
        self.assertNotEqual(response.status_code, 201)

    def test_placeorder(self):
        """Check if user is able to login"""
        response = self.client().post('/api/v1/signup', data={"email": self.email,
                                                              "password": self.password})
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
