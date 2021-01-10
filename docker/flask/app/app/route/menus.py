
import os
from . import api

from flask import jsonify, request, Blueprint
from flask_jwt_extended import (
    jwt_required, fresh_jwt_required,
    get_jwt_identity, get_raw_jwt
)

from app.model import UserOperater, ClientOperater, ChildClientOperater

prefix = '/'+str(os.path.basename(__file__)).replace('.py','')
UserOp = UserOperater()
ClientOp = ClientOperater()
ChildOp = ChildClientOperater()

@api.route(prefix)
@jwt_required
def index():
  data = UserOp.getUserFromID(get_jwt_identity())
  if data == []:
    return jsonify({'f_user_name': None}), 404

  return jsonify({'f_user_name': data['f_user_name'], 'clients': []}), 200

@api.route(prefix+'/create/regist', methods=['POST'])
@jwt_required
def regist():
  inputs = request.get_json()
  ClientOp.registClient(inputs)
  
