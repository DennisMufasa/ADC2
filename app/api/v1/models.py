"""docstring for classes"""
import json

class Users:
    """docstring for Users class"""

    def __init__(self):
        """docstring for class constructor"""
        self.username = ""
        self.email = ""
        self.password = ""
        self.phone = ""
        self.Users = []

    def add_user(self, cred):
        """docstring for add user method"""
        self.username = cred["name"]
        self.email = cred["email"]
        self.password = cred["password"]
        self.phone = cred["phone"]

        for user in self.Users:
            if user['email'] == self.email:
                return "That account already exists!"

        self.Users.append({"username": self.username,
                      "password": self.password,
                      "email": self.email,
                      "phone": self.phone})

        return "user added!"

    def get_user(self, name):
        """docstring for get one user method"""
        if not self.Users:
            return "There are no users registered!"
        for user in self.Users:
            if user["username"] != name:
                continue
            return user

    def get_all_users(self):
        """docstring for get all users method"""
        if not self.Users:
            return "There are no users registered!"
        return self.Users

    def validate_user(self, cred):
        """docstring for validate method"""
        for user in self.Users:
            if user['email'] == cred["email"] and user['password'] == cred["password"]:
                return "Validation Successful!"
        return "Invalid credentials"


class Menu:
    """docstring for food orders"""

    def __init__(self):
        self.Orders = []
        self.count = 1

    def place_order(self, order):
        """docstring place order method"""
        if not order:
            return "No order for food placed!"
        self.Orders.append({"OrderId":self.count,
                            "order": order,
                            "Accepted": True})

        self.count = self.count + 1
        return "Order placed Successfully!"

    def get_one_order(self, order_id):
        """docstring for get one order method"""
        if not self.Orders:
            return "No orders for food placed!"
        for order in self.Orders:
            if order["OrderId"] != order_id:
                continue
            return order

    def get_orders(self):
        """docstring for get all orders method"""
        if not self.Orders:
            return "No order for food placed!"
        return self.Orders

    def update_order_status(self, order_id):
        """docstring for update status method"""
        if not self.Orders:
            return "No order for food placed!"
        for order in self.Orders:
            if order["OrderId"] != order_id:
                continue
            order["Accepted"] = False
            return order
