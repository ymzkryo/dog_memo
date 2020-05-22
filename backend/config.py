import os

class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///backend.db'
    SECRET_KEY = os.urandom(24)
