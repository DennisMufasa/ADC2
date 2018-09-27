"""Docstring for config file"""

import os


class Config(object):
    """Docstring for config class"""
    DEBUG = True
    SECRET = os.getenv('SECRET')


class Development(Config):
    """Docstring for development class"""
    DEBUG = True


class Testing(Config):
    DEBUG = True
    TESTING = True


configuration = {
    'development':  Development,
    'testing': Testing
}