from flask import Blueprint

v1_blue_print = Blueprint('v1', __name__, url_prefix='/api/v1')

from . import view