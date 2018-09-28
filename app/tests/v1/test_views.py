"""Docstring for test_views"""
# system imports
import sys
sys.path.append("..")

# third party module imports
import unittest

# local imports
from ...api import create_app


class TestViews(unittest.TestCase):
    """Docstring for Test_views class"""

    def setUp(self):
        """set up the tests and the app"""

        self.app = create_app('testing')
        self.client = self.app.test_client
        self.email = 'mufasa@email.com'
        self.username = 'mufasa'
        self.password = 'mfs@18'
        self.phone = +254712736170
        self.food = 'burger'
        self.cost = 200
        self.id = 1

    def test_loggin(self):
        """test user login"""
        response = self.client().post('/api/v1/login', data={"email": self.email,
                                                             "password": self.password})

        self.assertEqual(response.status_code, 200)


    def test_placeorder(self):
        """Check if order is placed"""
        response = self.client().post('/api/v1/orders', data={"food": self.food,
                                                        "cost": self.cost})
        self.assertEqual(response.status_code, 201)

    def test_get_order(self):
        """Check if user is able to login"""
        response = self.client().get('/api/v1/orders')
        self.assertEqual(response.status_code, 200)

    def test_get_one_order(self):
        """Check a specific order is fetched"""
        response = self.client().get('/api/v1/orders/1')
        self.assertEqual(response.status_code, 200)

    def test_update_order(self):
        """Check if order is updatable"""
        response = self.client().put('/api/v1/orders/1')
        self.assertEqual(response.status_code, 201)

    

if __name__ == "__main__":
    unittest.main()
