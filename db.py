#!/usr/bin/env python3
""" The database"""
from mongoengine import connect


db_name = 'doctalk_db'

# Connection point
# Database security credentials not yet set
# My idea is to import the db on main.py...

def init_mongo():
    connect(db=db_name)
