#!/usr/bin/env python3
""" Chat room routes """

from flask import Blueprint
from views.chat_room import (
    create_room,
    get_rooms,
    get_chat_rooms,
    get_room,
    delete_room,
    add_user,
    update_room,
    remove_user
)

chat_room_bp = Blueprint('chat_room_routes', __name__, url_prefix='/chat_room')


@chat_room_bp.route("/room", methods=["POST"])
def create():
    """ creates a new chat room """
    return create_room()


@chat_room_bp.route("/room/<room_id>", methods=["GET"])
def get(room_id):
    """ get a specific chat room """
    return get_room(room_id)


@chat_room_bp.route("/room/<room_id>", methods=["DELETE"])
def delete(room_id):
    """ delete a chat room """
    return delete_room(room_id)


@chat_room_bp.route("/room/<room_id>/user/<user_id>", methods=["POST"])
def add(room_id, user_id):
    """ add a user to a chat room """
    return add_user(room_id, user_id)


@chat_room_bp.route("/room/<room_id>/user/<user_id>", methods=["DELETE"])
def remove(room_id, user_id):
    """ remove a user from a chat room """
    return remove_user(room_id, user_id)


@chat_room_bp.route("/rooms/<user_id>", methods=["GET"])
def get_rooms_for_user(user_id):
    """ get chat rooms for a specific user """
    return get_rooms(user_id)


@chat_room_bp.route("/rooms/<first_user_id>/<second_user_id>", methods=["GET"])
def get_chat_rooms(first_user_id, second_user_id):
    """ get chat rooms of two specific user """
    return get_chat_rooms(first_user_id, second_user_id)


@chat_room_bp.route("/room/<room_id>", methods=["PUT"])
def update(room_id):
    """ edit a chat room """
    return update_room(room_id)
