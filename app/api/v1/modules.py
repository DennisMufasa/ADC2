"""docstring for classes"""
import json

USERS = []
ORDERS = []


class Users(object):
    """docstring for Users class"""

    def __init__(self):
        """docstring for class constructor"""
        self.username = ""
        self.email = ""
        self.password = ""
        self.phone = ""

    def add_user(self, name, email, password, phone):
        """docstring for add user method"""
        self.username = name
        self.email = email
        self.password = password
        self.phone = phone

        for user in USERS:
            if user['email'] == self.email:
                return "That account already exists!"

        USERS.append({"username": self.username,
                      "password": self.password,
                      "email": self.email,
                      "phone": self.phone})

        return "user added!"

    @staticmethod
    def get_user(name):
        """docstring for get one user method"""
        if not USERS:
            return "Data set is empty"
        for user in USERS:
            if user["username"] == name:
                return json.dumps(user)

    @staticmethod
    def get_all_users():
        """docstring for get all users method"""
        if not USERS:
            return "data set is empty!"
        return json.dumps({"users:": USERS})

    @staticmethod
    def get_email():
        """docstring for get email method"""
        if not USERS:
            return "data set is empty"
        for user in USERS:
            email = user["email"]
            return email

    @staticmethod
    def validate_user(email, password):
        """docstring for valiadte method"""
        for user in USERS:
            if user['email'] == email and user['password'] == password:
                return "Validation Successfull!"
        return "Invalid credentials"


class Orders(Users):
    """docstring for class Orders method"""

    def place_order(self, food, cost):
        """docstring place order method"""
        if not USERS:
            return "Login first"
        new_order = {super(Orders, self).get_email(): {"food": food, "cost": cost, "accepted": True}}
        ORDERS.append(new_order)
        return "new order placed"

    def get_one_order(self, food):
        """docstring for get one order method"""
        if not ORDERS:
            return "Data set is empty!"
        for order in ORDERS:
            if order[super(Orders, self).get_email()]["food"] == food:
                return json.dumps({"food:": order[super(Orders, self).get_email()]["food"],
                                   "cost:": order[super(Orders, self).get_email()]["cost"]})
            return "Sorry order not available!"

    @staticmethod
    def get_orders():
        """docstring for get all orders method"""
        if not ORDERS:
            return "Data set empty!"
        return json.dumps({"orders:": ORDERS})

    def update_order_status(self, food):
        """docstring for update status method"""
        if not ORDERS:
            return "Data set is empty!"
        for order in ORDERS:
            if order[super(Orders, self).get_email()]["food"] == food:
                order[super(Orders, self).get_email()]["accepted"] = False
                return json.dumps({"update: ": order})


