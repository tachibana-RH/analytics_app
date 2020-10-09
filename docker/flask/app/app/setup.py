import os
import redis
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# Setup our redis connection for storing the blacklisted tokens
revoked_store = redis.StrictRedis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=int(os.getenv('REDIS_PORT', '6379')),
    db=0,
    decode_responses=True
    )

#Setup mysql connection
db = SQLAlchemy()
msmlw = Marshmallow()
def init_db(app):
    db.init_app(app)
    Migrate(app, db)