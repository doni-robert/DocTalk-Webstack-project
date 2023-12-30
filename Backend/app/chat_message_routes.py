#!/usr/bin/env python3
""" Routes for chat messages """

from flask import Blueprint
from views.chat_message import (
    create_message,
    get_messages,
    delete_message,
    update_message
)


chat_message_bp = Blueprint('chat_message_routes', __name__, url_prefix='/chat_message')


@chat_message_bp.route("/message", methods=["POST"])
def create():
    """ creates a new message """
    return create_message()


@chat_message_bp.route("/message/<chat_room_id>", methods=["GET"])
def get(chat_room_id):
    """ get messages for a specific chat room """
    return get_messages(chat_room_id)


@chat_message_bp.route("/message/<message_id>", methods=["PUT"])
def update(message_id):
    """ edit a message """
    return update_message(message_id)


@chat_message_bp.route("/message/<message_id>", methods=["DELETE"])
def delete(message_id):
    """ delete a message """
    return delete_message(message_id)
