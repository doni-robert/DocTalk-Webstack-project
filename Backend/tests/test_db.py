#!/usr/bin/env python3
""" Contains the TestDatabaseInitialization class"""
import unittest
from flask import Flask
from config import TestConfig
from db import init_mongodb


class TestDatabaseInitialization(unittest.TestCase):
    """Tests to check the initialization of the database"""

    def test_database_initialization(self):
        """Test whether database was successfully initialized"""
        app = Flask(__name__)
        app.config.from_object(TestConfig)

        try:
            init_mongodb(app)
        except Exception as e:
            self.fail(e)

        self.assertTrue(True)
