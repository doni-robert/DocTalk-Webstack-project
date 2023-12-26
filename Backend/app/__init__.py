#!/usr/bin/env python3
""" Makes the app folder a package"""

from flask import Flask
from config import Config
from db import init_mongodb
from flask_jwt_extended import JWTManager
from . import auth, chat_room_routes, chat_message_routes


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

# app routes
app.register_blueprint(auth.bp)
app.register_blueprint(chat_room_routes.room_bp)
app.register_blueprint(chat_message_routes.chats_bp)

# database initialization
init_mongodb(app)

# JWT
JWTManager(app)

from app import auth, chat_room_routes, chat_message_routes
