"""Docstring for run.py"""
# system import
import os

# local import
from . app.api import create_app

config_key = os.getenv('APP_SETTINGS')

app = create_app(config_key)

if __name__ == "__main__":
    app.run()


