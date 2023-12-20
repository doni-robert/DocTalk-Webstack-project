#!/usr/bin/env python3
""" Makes the app folder a package"""

from flask import Flask
from config import Config
from db import init_mongodb
from flask_jwt_extended import JWTManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

init_mongodb(app)

JWTManager(app)

from app import views
