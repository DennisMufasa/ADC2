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

    return Orders().place_order(food, cost), 201


@v1_blue_print.route('/signup', methods=['POST'])
def update():
    """sign up new users"""
    username = request.form['name']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']

    Orders().add_user(username, email, password, phone)

    return make_response(Orders().get_user(username)), 201


@v1_blue_print.route('/login', methods=['POST'])
def login():
    """login for all users"""

    email = request.form['email']
    password = request.form['pass']

    if email == "admin@email.com" and password == "admin":
        return make_response("welcome admin!"), 200

    return Orders().validate_user(email, password), 200


@v1_blue_print.route('/orders', methods=['GET'])
def fetch_all_orders():
    """fetch all data"""
    return Orders().get_orders(), 200


@v1_blue_print.route('/orders/<string:food>', methods=['GET'])
def fetch_one_order(food):
    """fetch one order based on food"""
    return Orders().get_one_order(food), 200


@v1_blue_print.route('/update/<string:food>', methods=['PUT'])
def update_status(food):
    """fetch a specific order and changes any of its values"""

    return Orders().update_order_status(food), 201


@v1_blue_print.route('/show', methods=['GET'])
def fetch_all():
    """fetch all users"""
    return Orders().get_all_users(), 200


@v1_blue_print.route('/show/<string:name>', methods=['GET'])
def fetch_one(name):
    """fetch a specific user's details based on name"""
    return Orders().get_user(name), 200
