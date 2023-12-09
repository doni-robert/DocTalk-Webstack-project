#!/usr/bin/env python3
"""
This module contains the configurations for Flask-SQLAlchemy
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    This class contains the configurations for Flask-SQLAlchemy
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('YOUR_FLASK_SECRET_KEY', 'default_secret_key')
