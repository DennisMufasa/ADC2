"""Docstring for run.py"""
# system import
import os

# local import
from .app.api import create_app

app = create_app('development')

if __name__ == "__main__":
    app.run()


