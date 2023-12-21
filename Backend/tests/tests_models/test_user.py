#!/usr/bin/env python3
""" Contains the TestUserClass class"""
import unittest
from flask import Flask
from db import init_mongodb
from models.user import User


class TestUserClass(unittest.TestCase):
    "Tests to check creation and storage of a user"
    
    def setUp(self):
        """ Sets up a flask app and connects to the db"""
        app = Flask(__name__)
        app.config['DB_HOST'] = 'mongodb://localhost:27017/test_database'
        init_mongodb(app)

    def test_user_creation(self):
        """ Test creation of a user"""
        user = User(email="john@example.com", name="John Doe", password="password123")
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.password, "password123")

    def test_save_user(self):
        "Tests storing of a user"
        new_user = User.save_user(email="jane@example.com", name="Jane Doe", password="securepass")
        self.assertIsNotNone(new_user.id)