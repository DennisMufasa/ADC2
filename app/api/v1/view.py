"""Docstring for endpoints"""
from flask import request, make_response, jsonify
from .models import Users,Menu
from . import v1_blue_print

USER = Users()
FOOD_ORDER = Menu()

# routes
@v1_blue_print.route('/orders', methods=['GET','POST'])
def orders():
    """posting data from a form to server"""
    if request.method == 'POST':
        request_data = request.get_json()
        return make_response(jsonify({"Message": FOOD_ORDER.place_order(request_data)}), 201)

    return make_response(jsonify({"Message": FOOD_ORDER.get_orders()}, 200))


@v1_blue_print.route('/orders/<int:orderId>', methods=['GET'])
def fetch_one_order(orderId):
    """fetch one order based on order id"""
    return make_response(jsonify({"Message": FOOD_ORDER.get_one_order(orderId)}), 200)


@v1_blue_print.route('/orders/<int:orderId>', methods=['PUT'])
def update_status(orderId):
    """fetch a specific order and changes any of its values"""
    return make_response(jsonify({"Message": FOOD_ORDER.update_order_status(orderId)}), 201)

@v1_blue_print.route('/signup', methods=['POST'])
def update():
    """sign up new users"""
    request_data = request.get_json()
    return make_response(jsonify({"Message": USER.add_user(request_data)}), 201)


@v1_blue_print.route('/login', methods=['POST'])
def login():
    """login for all users"""
    request_data = request.get_json()
    return make_response(jsonify({"Message": USER.validate_user(request_data)}), 200)


@v1_blue_print.route('/users', methods=['GET'])
def fetch_all():
    """fetch all users"""
    return make_response(jsonify({"Message": USER.get_all_users()}), 200)


@v1_blue_print.route('/user/<string:name>', methods=['GET'])
def fetch_one(name):
    """fetch a specific user's details based on name"""
    return make_response(jsonify({"Message": USER.get_user(name)}), 200)
