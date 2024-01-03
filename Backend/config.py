#!/usr/bin/env python3
""" Configuration file """

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'xyzxyz xyzxyz xyzxyz')


class DevConfig(Config):
    """ Development Configuration class """
    MONGODB_SETTINGS = {
        'db': os.environ.get("MONGODB_DB", "dev_db"),
        'host': os.environ.get("MONGODB_HOST", "localhost"),
        'port': os.environ.get("MONGODB_PORT", 27017)
    }
    DEBUG = True


class ProdConfig(Config):
    """ Production Configuration class """
    pass


class TestConfig(Config):
    """ Testing Configuration class """
    MONGODB_SETTINGS = {
        'db': "test_db",
        'host': "localhost",
        'port': 27017
    }
    TESTING = True
