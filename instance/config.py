"""Docstring for config file"""

import os

# get top-level directory of project
BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = os.urandom(24)
DEVELOPMENT = True
