"""Docstring for app config"""
from flask import Flask


# app factory. Initializes a new app on call with an arg config filename
def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    return app


