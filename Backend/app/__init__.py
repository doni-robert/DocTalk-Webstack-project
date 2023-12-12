#!/usr/bin/env python3
""" Makes the app folder a package"""

from flask import Flask
from config import Config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

from app import views
