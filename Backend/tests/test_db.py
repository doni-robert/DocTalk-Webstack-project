#!/usr/bin/env python3
""" Contains the TestDatabaseInitialization class"""
import unittest
from unittest.mock import patch
from flask import Flask
from db import init_mongodb


class TestDatabaseInitialization(unittest.TestCase):
    """Tests to check the initialization of the database"""

    def test_database_initialization(self):
        """Test whether database was successfully initialized"""
        app = Flask(__name__)
        app.config['DB_HOST'] = 'mongodb://localhost:27017/test_database'

        try:
            init_mongodb(app)
        except Exception as e:
            self.fail(e)

        self.assertTrue(True)
