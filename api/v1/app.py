"""Docstring for fast food fast api endpoints"""
import datetime
import sys
from flask import Flask, jsonify, request, make_response
from data_store import ORDERS

# adding the parent dir to sys.path to allow importation of data_store
sys.path.append('../')  # i put this here to satisfy pep8 style guid


APP = Flask(__name__)


@APP.route('/api/v1/order', methods=['POST'])
def make_order():
    """make a new order"""
    new_order = request.get_json()  # fetches data from client in json format

    # new_order = json.loads(order)   # convert the json data to a python dict.

    index = len(ORDERS.items())

    # creating order details to save to ORDERS
    save_order = {index: {"id": index + 1,
                          "user": new_order['user'],
                          "order": {"food": new_order['order']['food'],
                                    "cost": new_order['order']['cost']},
                          "date": str(datetime.datetime.now())}
                  }

    ORDERS.update(save_order)  # saving new order

    # 20 is the status code for created
    return make_response(jsonify({"Order placed": save_order}), 201)


if __name__ == '__main__':
    APP.run(debug=True)
