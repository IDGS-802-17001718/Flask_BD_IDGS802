import os 
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY='SECRET'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='myqls+pymysql://mario_admin:12345678@localhost/bd_idgs802'

