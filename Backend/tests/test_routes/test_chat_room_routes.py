#!/usr/bin/env python3
""" Contains the test class for the chat room routes """

import unittest
from unittest.mock import patch
from flask import Flask
from config import TestConfig
from db import init_mongodb
from models import chat_room
from app.chat_room_routes import *
from app.auth import login
from app.chat_room_routes import room_bp
from app.auth import bp as auth_bp
from mongoengine.connection import get_db

    
def clear_db():
    """ Clears test_db before each test run """
    db = get_db()
    for collection in db.list_collection_names():
        if not collection.startswith("system."):
            db.drop_collection(collection)

class TestChatRoomRoutes(unittest.TestCase):
    """ Tests for chat room routes """

    def setUp(self):
        """ Sets up the test client """
        self.app = Flask(__name__)
        self.app.config.from_object(TestConfig)
        self.client = self.app.test_client()

        self.app.register_blueprint(room_bp)
        self.app.register_blueprint(auth_bp)

        with self.app.app_context():
            init_mongodb(self.app)
            clear_db()

    def login_user(self):
        """ Helper function to log in a user and return an access token """
        with patch.object(User, 'get_user_by_email') as mock_get_user_by_email, \
        patch('werkzeug.security.check_password_hash') as mock_check_password_hash:
            mock_check_password_hash.return_value = True
            mock_user = User()
            mock_user.password = 'testpassword'
            mock_user.email = 'testuser@example.com'
            mock_get_user_by_email.return_value = mock_user

            response = self.client.post("/auth/login/", json={
                "email": "testuser@example.com",
                "password": "testpassword"
            })

            print(response.get_data(as_text=True))
            # print(mock_get_user_by_email.called)
            print(mock_get_user_by_email.return_value)
            print(mock_user)
            print(mock_user.password)
            # print(mock_check_password_hash.called)
            # print(mock_check_password_hash.call_args)

            return response.get_json()["access_token"]


    @patch.object(chat_room.ChatRoom, 'create_room')
    @patch.object(chat_room.ChatRoom, 'get_room_by_name')
    @patch('app.chat_room_routes.logged_in')
    def test_create_room(self, mock_logged_in, mock_get_room_by_name, mock_create_room):
        """ Tests the create_room route """
        mock_logged_in.return_value = lambda f: f
        mock_get_room_by_name.return_value = None
        mock_create_room.return_value = ChatRoom()

        access_token = self.login_user()

        headers = {"Authorization": f"Bearer {access_token}"}

        response = self.client.post('/rooms/create_room',
                                    json={"room_name": "testroom"},
                                    headers=headers
                                    )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"message": "Room testroom created successfully"})
