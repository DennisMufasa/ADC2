"""Docstring for endpoints"""
from flask import request, make_response
from .models import Orders
from . import v1_blue_print


# routes
@v1_blue_print.route('/', methods=['POST'])
def home():
    """posting data from a form to server"""
    food = request.form['food']
    cost = request.form['cost']

    return Orders().place_order(food, cost)


@v1_blue_print.route('/signup', methods=['POST'])
def update():
    """sign up new users"""
    username = request.form['name']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']

    Orders().add_user(username, email, password, phone)

    return make_response(Orders().get_user(username))

