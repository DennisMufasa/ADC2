"""Docstring for test_views"""
# system import
import os

# thirdparty module imports
import unittest
import json

# local imports
from app.api import create_app


class Test_views(unittest.TestCase):
    """Docstring for Test_views class"""

    def setUp(self):
        """set up the tests and the app"""

        self.app = create_app(config_filename='testing')
        self.client = self.app.test_client
        self.food = 'burger'
        self.cost = 200

    def test_placeorder_without_loggin(self):
        """Check if the request is possible if not logged on"""
        resposnse = self.client().post('/api/v1/', data={"food": self.food,
                                                         "cost": self.cost})
        self.assertEqual(resposnse.status_code, 201)
