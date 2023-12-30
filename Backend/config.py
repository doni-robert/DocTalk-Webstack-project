#!/usr/bin/env python3
""" Configuration file """

import os


class Config:
    """ Configuration class """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xyzxyz xyzxyz xyzxyz'
    DB_HOST = os.environ.get('DB_HOST') or 'mongodb://localhost:27017/doctalk_db'
