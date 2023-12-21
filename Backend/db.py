#!/usr/bin/env python3
""" The database"""
from mongoengine import connect


def init_mongodb(app):
    """
    Database initialization
    """
    try:
        db_uri = app.config['DB_HOST']
        connect(host=db_uri, uuidRepresentation='standard')
    except Exception as e:
        raise e
