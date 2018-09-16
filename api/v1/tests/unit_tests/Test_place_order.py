"""Docstring for test_place_order"""
import pytest

from api.v1.app import APP


def test_place_order():
    """test if orders are posted to the server"""
    response = APP.test_client().post('/api/v1/order',
                                      json={"user": "mufasa",
                                            "order": {"food": "burger",
                                                      "cost": 250}})

    assert response.status_code == 201
