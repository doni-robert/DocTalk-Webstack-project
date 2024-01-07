#!/usr/bin/env python3
""" The database"""
from mongoengine import connect, disconnect


def init_mongodb(app):
    """
    Database initialization
    """
    try:
        """
        - disconnects the default connection before establishing a new one
        - default connection is the TestConfig connection
        """
        disconnect(alias="default")

        db_uri = (
            f"mongodb://{app.config['MONGODB_SETTINGS']['host']}:"
            f"{app.config['MONGODB_SETTINGS']['port']}/"
            f"{app.config['MONGODB_SETTINGS']['db']}"
        )
        connect(host=db_uri, uuidRepresentation='standard')
    except Exception as e:
        raise e
