#!/usr/bin/env python3
""" The database"""
from mongoengine import connect


def init_mongodb(app):
    """
    Database initialization
    """
    db_uri = app.config['DB_HOST']
    connect(host=db_uri)
