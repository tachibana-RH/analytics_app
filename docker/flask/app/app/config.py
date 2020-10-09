"""FlaskのConfigを提供する"""
import os
from datetime import timedelta

# Setup the flask-jwt-extended extension. See:
ACCESS_EXPIRES = timedelta(minutes=15)
REFRESH_EXPIRES = timedelta(days=30)

class DevelopmentConfig:

  # Flask
  DEBUG = True

  # Configure application to store JWTs in cookies. Whenever you make
  # a request to a protected endpoint, you will need to send in the
  # access or refresh JWT via a cookie.
  JWT_TOKEN_LOCATION = ['cookies']

  # Only allow JWT cookies to be sent over https. In production, this
  # should likely be True
  JWT_COOKIE_SECURE = os.getenv('COOKIE_SECURE', False)

  # Set the cookie paths, so that you are only sending your access token
  # cookie to the access endpoints, and only sending your refresh token
  # to the refresh endpoint. Technically this is optional, but it is in
  # your best interest to not send additional cookies in the request if
  # they aren't needed.
  JWT_ACCESS_COOKIE_PATH = '/api/'
  JWT_REFRESH_COOKIE_PATH = '/api/v1/auth'

  # Enable csrf double submit protection. See this for a thorough
  # explanation: http://www.redotheweb.com/2015/11/09/api-security.html
  JWT_COOKIE_CSRF_PROTECT = True

  JWT_SECRET_KEY = 'super-secret'  # Change this!
  JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
  JWT_REFRESH_TOKEN_EXPIRES = REFRESH_EXPIRES
  JWT_BLACKLIST_ENABLED = True
  JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

  # SQLAlchemy
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/StatisticalAnalysis?charset=utf8'.format(**{
      'user': os.getenv('DB_USER', 'root'),
      'password': os.getenv('DB_PASSWORD', 'root'),
      'host': os.getenv('DB_HOST', 'localhost'),
      'port': os.getenv('DB_PORT', '3306')
  })
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False

class ProductionConfig:

  # Flask
  DEBUG = False

  JWT_SECRET_KEY = 'super-secret'  # Change this!
  JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
  JWT_REFRESH_TOKEN_EXPIRES = REFRESH_EXPIRES
  JWT_BLACKLIST_ENABLED = True
  JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

  # SQLAlchemy
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/StatisticalAnalysis?charset=utf8'.format(**{
      'user': os.getenv('DB_USER', 'root'),
      'password': os.getenv('DB_PASSWORD', 'root'),
      'host': os.getenv('DB_HOST', 'localhost'),
      'port': os.getenv('DB_PORT', '3306')
  })
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False


DevConfig = DevelopmentConfig
ProConfig = ProductionConfig