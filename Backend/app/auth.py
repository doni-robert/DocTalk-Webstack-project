#!/usr/bin/env python3
""" Handles authentication routes """

from flask import Blueprint, request, jsonify, make_response
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register/', methods=['POST'])
def register():
    """ Registers a new user """
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = generate_password_hash(data.get("password"))

    if not username or not email or not password:
        return make_response(
            jsonify({"message": "Missing username, email or password"}),
            400)

    if User.get_user_by_email(email):
        return jsonify(
            {"message": f"User with email {email} already exists"})

    new_user = User.create_user(email, username, password)
    return make_response(
            jsonify({"message": f"User created successfuly"}),
            201)


@bp.route('/login/', methods=['POST'])
def login():
    """ Logs in an existing user """
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = User.get_user_by_email(email)
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.name)
        refresh_token = create_refresh_token(identity=user.name)

        return jsonify(
            {"access_token": access_token, "refresh_token": refresh_token}
        )

    else:
        return jsonify({"message": "Invalid username or password"})


@bp.route('/logout', methods=['GET'])
def logout():
    """ Logs out a user """
    return jsonify({"message": "Logged out successfully"})
