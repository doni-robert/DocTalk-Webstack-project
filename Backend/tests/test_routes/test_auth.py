#!/usr/bin/env python3
""" Contains test classes for user authentication routes """

import unittest
from unittest.mock import patch
from flask import Flask
from config import TestConfig
from db import init_mongodb
from app.auth import *
from app.auth import bp as auth_bp
from mongoengine.connection import get_db


def clear_db():
    """ Clears test_db before each test run """
    db = get_db()
    for collection in db.list_collection_names():
        if not collection.startswith("system."):
            db.drop_collection(collection)


class TestAuth(unittest.TestCase):
    """ Tests for user authentication routes"""
    def setUp(self):
        """ Sets up the test client and initializes the database"""
        self.app = Flask(__name__)
        self.app.config.from_object(TestConfig)
        self.client = self.app.test_client()

        self.app.register_blueprint(auth_bp)

        with self.app.app_context():
            init_mongodb(self.app)
            clear_db()

    # Tests for /register/ route
    @patch.object(User, 'create_user')
    def test_register_success(self, mock_create_user):
        """ Tests User Registration Action """
        mock_create_user.return_value = User()

        response = self.client.post('/auth/register/', json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        })

        # print(response.get_json())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"message": "User created successfully"})

    @patch.object(User, 'get_user_by_email')
    def test_register_existing_user(self, mock_get_user_by_email):
        """ Tests User Registration Action when user already exists """
        mock_get_user_by_email.return_value = User()

        response = self.client.post('/auth/register/', json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(),
                         {"message": "User with email testuser@example.com already exists"})

    def test_register_missing_fields(self):
        """ Tests User Registration Action when fields are missing """
        response = self.client.post('/auth/register/', json={
            "username": "testuser",
            "email": "testuser@example.com"
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {"message": "Missing username, email or password"})

    # Tests for /login/ route
    @patch.object(User, 'get_user_by_email')
    @patch('werkzeug.security.check_password_hash')
    def test_login_success(self, mock_check_password_hash, mock_get_user_by_email):
        """ Tests User Login Action """
        mock_check_password_hash.return_value = True
        mock_user = User()
        mock_user.password = 'mock_password'
        mock_get_user_by_email.return_value = mock_user

        response = self.client.post('/auth/login/', json={
            "email": "testuser.example.com",
            "password": "testpassword"
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Login successful"})
        self.assertEqual(response.get_json()['access_token'], '<mocked access token>')
        self.assertEqual(response.get_json()['refresh_token'], '<mocked refresh token>')

    @patch.object(User, 'get_user_by_email')
    @patch('werkzeug.security.check_password_hash')
    def test_login_invalid_credentials(self, mock_check_password_hash, mock_get_user_by_email):
        """ Test for invalid credentials when user is logging in """
        mock_check_password_hash.return_value = False
        mock_get_user_by_email.return_value = User()

        response = self.client.post('/auth/login/', json={
            "email": "testuser.example.com",
            "password": "testpassword"
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {"message": "Invalid username or password"})

    # Tests for /logout route
    def test_logout_success(self):
        """ Test for successful logout """
        response = self.client.get('/auth/logout')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Logged out successfully"})


if __name__ == '__main__':
    unittest.main()
