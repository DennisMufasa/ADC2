"""Docstring for endpoints"""
from flask import request
from .models import Orders
from . import v1_blue_print


# routes
@v1_blue_print.route('/', methods=['POST'])
def home():
    """posting data from a form to server"""
    food = request.form['food']
    cost = request.form['cost']

    return Orders().place_order(food, cost)
