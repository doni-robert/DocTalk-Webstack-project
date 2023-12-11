#!/usr/bin/env python3
""" Configuration file """

import os

class Config:
    """ Configuration class """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xyzxyz xyzxyz xyzxyz'
