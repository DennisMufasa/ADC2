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


@v1_blue_print.route('/login', methods=['POST'])
def login():
    """login for all users"""

    email = request.form['email']
    password = request.form['pass']

    if email == "admin@email.com" and password == "admin":
        return make_response("welcome admin!")

    return Orders().validate_user(email, password)


@v1_blue_print.route('/orders', methods=['GET'])
def fetch_all_orders():
    """fetch all data"""
    return Orders().get_orders()


