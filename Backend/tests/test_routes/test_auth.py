#!/usr/bin/env python3
""" Contains test classes for user authentication routes """

import unittest
from unittest.mock import patch
from app.auth import *
from . import BaseTestCase


class TestAuth(BaseTestCase):
    """ Tests for user authentication routes"""

    """ ------- Tests for /register/ route -------"""
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

    """ ------- Tests for /login/ route -------"""
    @patch.object(User, 'get_user_by_email')
    @patch('werkzeug.security.check_password_hash')
    def test_login_success(self, mock_check_password_hash, mock_get_user_by_email):
        """ Tests User Login Action """
        mock_check_password_hash.return_value = True
        mock_user = User()
        mock_user.password = 'scrypt:32768:8:1$kKffHgKnFebre5af$d0475c61e82a0552253bfe2e8a8ab358f7b7bc03a72286f13eb6703353bafb26358b37bdfd3c59c224c3046fdb8c009d4cccb63ff7824b3846216abcdc9269d9'
        mock_get_user_by_email.return_value = mock_user

        # mock access and refresh tokens
        mock_access_token = '<mocked access token>'
        mock_refresh_token = '<mocked refresh token>'

        # patch create_access_token and create_refresh_token functions
        with patch('app.auth.create_access_token') as mock_create_access_token, \
                patch('app.auth.create_refresh_token') as mock_create_refresh_token:
            mock_create_access_token.return_value = mock_access_token
            mock_create_refresh_token.return_value = mock_refresh_token
            response = self.client.post('/auth/login/', json={
                "email": "testuser.example.com",
                "password": "testpassword"
            })

        # print(response.get_json())
        # print(mock_get_user_by_email.return_value)
        # print(mock_user)
        # print(mock_user.password)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            "access_token": mock_access_token,
            "message": "Login successful",
            "refresh_token": mock_refresh_token
        })

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

    """ ------- Tests for /logout/ route -------"""
    def test_logout_success(self):
        """ Test for successful logout """
        response = self.client.get('/auth/logout')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Logged out successfully"})


if __name__ == '__main__':
    unittest.main()
