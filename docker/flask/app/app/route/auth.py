import os
from . import api

from flask import jsonify, request, Blueprint
from flask_jwt_extended import (
    jwt_required, fresh_jwt_required, jwt_refresh_token_required,
    create_access_token, create_refresh_token,
    get_jwt_identity, get_raw_jwt, get_jti,
    set_access_cookies, set_refresh_cookies, unset_jwt_cookies
)

from app.model import UserOperater
from app.setup import revoked_store
from app.config import ACCESS_EXPIRES, REFRESH_EXPIRES
from datetime import timedelta


prefix = '/'+str(os.path.basename(__file__)).replace('.py','')
UserTb = UserOperater()

@api.route(prefix+'/signup', methods=['POST'])
def signup():
    username = request.json.get('f_user_name', None)
    password = request.json.get('f_password', None)
    model = {'f_user_name': username, 'f_password': password}

    if UserTb.isExistUser(user=model):
        return jsonify({"msg": "this username is already exist"}), 401
    
    result = UserTb.registUser(user=model)
    return jsonify({'signup': True}), 201


# Standard login endpoint. Will return a fresh access token and
# a refresh token
@api.route(prefix+'/signin', methods=['POST'])
def signin():
    username = request.json.get('f_user_name', None)
    password = request.json.get('f_password', None)
    model = {'f_user_name': username, 'f_password': password}

    if UserTb.isUnAuthUser(user=model):
        return jsonify({"msg": "Bad username or password"}), 401

    # Store the tokens in redis with a status of not currently revoked. We
    # can use the `get_jti()` method to get the unique identifier string for
    # each token. We can also set an expires time on these tokens in redis,
    # so they will get automatically removed after they expire. We will set
    # everything to be automatically removed shortly after the token expires
    user = UserTb.getUser(user=model)
    access_token = create_access_token(identity=user['f_user_id'], fresh=True)
    refresh_token = create_refresh_token(identity=user['f_user_id'])

    access_jti = get_jti(encoded_token=access_token)
    refresh_jti = get_jti(encoded_token=refresh_token)
    revoked_store.set(access_jti, 'false', ACCESS_EXPIRES*1.2)
    revoked_store.set(refresh_jti, 'false', REFRESH_EXPIRES*1.2)

    resp = jsonify({'signin': True})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)

    return resp, 201


# Refresh token endpoint. This will generate a new access token from
# the refresh token, but will mark that access token as non-fresh,
# as we do not actually verify a password in this endpoint.
@api.route(prefix+'/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_userid = get_jwt_identity()
    new_token = create_access_token(identity=current_userid, fresh=False)
    access_jti = get_jti(encoded_token=new_token)
    revoked_store.set(access_jti, 'false', ACCESS_EXPIRES*1.2)

    resp = jsonify({'refresh': True})
    set_access_cookies(resp, new_token)
    
    return resp, 201


# Fresh login endpoint. This is designed to be used if we need to
# make a fresh token for a user (by verifying they have the
# correct username and password). Unlike the standard login endpoint,
# this will only return a new access token, so that we don't keep
# generating new refresh tokens, which entirely defeats their point.
@api.route(prefix+'/fresh-login', methods=['POST'])
def fresh_signin():
    username = request.json.get('f_user_name', None)
    password = request.json.get('f_password', None)
    model = {'f_user_name': username, 'f_password': password}

    if User.isUnAuthUser(model):
        return jsonify({"msg": "Bad username or password"}), 401
    
    user = User.getUser(model.f_user_name)
    new_token = create_access_token(identity=user.f_user_id, fresh=True)
    access_jti = get_jti(encoded_token=new_token)
    revoked_store.set(access_jti, 'false', ACCESS_EXPIRES*1.2)

    resp = jsonify({'fresh_signin': True})
    set_access_cookies(resp, new_token)

    return resp, 201


@api.route(prefix+'/create-dev-token', methods=['POST'])
@jwt_required
def create_dev_token():
    userid = get_jwt_identity()
    expires = timedelta(days=365)
    token = create_access_token(userid, expires_delta=expires, fresh=True)
    jti = get_jti(encoded_token=token)
    revoked_store.set(jti, 'false', expires*1.2)
    return jsonify({'token': token}), 201


# Endpoint for revoking the current users access token
@api.route(prefix+'/signout', methods=['DELETE'])
@jwt_required
def signout():
    jti = get_raw_jwt()['jti']
    revoked_store.set(jti, 'true', ACCESS_EXPIRES*1.2)
    resp = jsonify({'signout': True})

    return resp, 200


# Endpoint for revoking the current users refresh token
@api.route(prefix+'/signout_refresh', methods=['DELETE'])
@jwt_refresh_token_required
def signout_refresh():
    jti = get_raw_jwt()['jti']
    revoked_store.set(jti, 'true', REFRESH_EXPIRES*1.2)

    resp = jsonify({'signout': True})
    unset_jwt_cookies(resp)

    return resp, 200
