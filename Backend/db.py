#!/usr/bin/env python3
""" The database"""
from mongoengine import connect


def init_mongodb(app):
    """
    Database initialization
    """
    # db_uri = app.config['MONGODB_SETTINGS']
    connect(host='mongodb://localhost:27017/doctalk_db')
