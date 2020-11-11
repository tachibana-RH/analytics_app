
import os
from . import api

from flask import jsonify, Blueprint
from flask_jwt_extended import (
    jwt_required, fresh_jwt_required,
    get_jwt_identity, get_raw_jwt
)

from app.model import UserOperater

prefix = '/'+str(os.path.basename(__file__)).replace('.py','')
UserTb = UserOperater()

@api.route(prefix)
@jwt_required
def index():
  data = UserTb.getUserFromID(get_jwt_identity())
  if data == []:
    return jsonify({'name': None}), 404

  return jsonify({'name': data['name'], 'clients': []}), 200