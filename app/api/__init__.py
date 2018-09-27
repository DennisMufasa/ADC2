"""Docstring for app config"""
# third party import
from flask import Flask

# local import
from app.instance.config import configuration


# app factory. Initializes a new app on call with an arg config filename
def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configuration[config_filename])

    # local import
    from . v1 import v1_blue_print
    
    app.register_blueprint(v1_blue_print)

    return app

