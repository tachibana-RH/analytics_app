import os

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from .setup import revoked_store, init_db
import app.model

app = Flask(__name__)

# https://flask-cors.readthedocs.io/en/latest/api.html
CORS(app, resources={
    r"/api/*": {
        "origins": os.getenv('CLIENT_ORIGIN', 'http://localhost:51080'),
        'supports_credentials': True
        }
    })

conf = 'DevConfig' if os.getenv('FLASK_ENV', 'development') == 'development' else 'ProConfig'
app.config.from_object('app.config.' + conf)
init_db(app)
jwt = JWTManager(app)

# Create our function to check if a token has been blacklisted. In this simple
# case, we will just store the tokens jti (unique identifier) in redis
# whenever we create a new token (with the revoked status being 'false'). This
# function will return the revoked status of a token. If a token doesn't
# exist in this store, we don't know where it came from (as we are adding newly
# created tokens to our store with a revoked status of 'false'). In this case
# we will consider the token to be revoked, for safety purposes.
@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    jti = decrypted_token['jti']
    entry = revoked_store.get(jti)
    if entry is None:
        return True
    return entry == 'true'


# Using the expired_token_loader decorator, we will now call
# this function whenever an expired but otherwise valid access
# token attempts to access an endpoint
@jwt.expired_token_loader
def my_expired_token_callback(expired_token):
    token_type = expired_token['type']
    return jsonify({
        'status': 401,
        'sub_status': 42,
        'msg': 'The {} token has expired'.format(token_type)
    }), 401

from .route import api
app.register_blueprint(api, url_prefix='/api/v1')


print('app environment: %s' % (os.getenv('FLASK_ENV', 'development')))
print('client origins: %s' % (os.getenv('CLIENT_ORIGIN', 'http://localhost:51080')))