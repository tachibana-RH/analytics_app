from flask import Blueprint
import os

api = Blueprint('api', __name__)

from . import auth, menu, master