#!/usr/bin/env python3
""" Routes for chat messages """

from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from datetime import datetime
from models.chat_message import ChatMessage
from models.chat_room import ChatRoom

chats_bp = Blueprint('chat_message_routes', __name__, url_prefix='/chats')


# user must be logged in to chat
def logged_in(func):
    @wraps(func)
    @jwt_required()
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        return func(current_user, *args, **kwargs)
    return wrapper


@chats_bp.route('/send_message', methods=['POST'])
@logged_in
def send_message(current_user):
    """ Sends a message to a chat room """
    data = request.get_json()

    message = data.get('message')
    room_name = data.get('room_name')
    receiver_name = data.get('receiver_name')

    if not message or not room_name or not receiver_name:
        return make_response(
            jsonify(
                {"message": "Missing message, room name or receiver name"}),
            400)

    room = ChatRoom.get_room_by_name(room_name)
    if not room:
        return make_response(
            jsonify({"message": "Room not found"}),
            404)

    receiver = ChatRoom.get_user_by_name(receiver_name)
    if not receiver:
        return make_response(
            jsonify({"message": "Receiver not found"}),
            404)

    new_message = ChatMessage.create_message(message,
                                             current_user,
                                             receiver, room)
    return make_response(
        jsonify({"message": "Message sent successfuly"}),
        201)


@chats_bp.route('/get_messages/<chat_room_name>', methods=['GET'])
@logged_in
def get_messages(current_user, chat_room_name):
    """ Gets all messages from a chat room """
    # check if chatroom exists and the user is part of it
    room = ChatRoom.get_room_by_name(chat_room_name)
    if room is None or current_user not in room.users:
        return make_response(
            jsonify({"message": "Room not found or user not in room"}),
            404)

    # get all messages from the chat room
    messages = ChatMessage.get_messages_by_room(chat_room_name)

    # send the messages back
    return jsonify(
        {"messages": [message.to_dict() for message in messages]}), 200


@chats_bp.route('/update/<message_id>', methods=['PUT'])
@logged_in
def update(current_user, message_id):
    """ Updates a message in a chat room """
    # check if user exists and the message is from them
    message = ChatMessage.objects(id=message_id).first()
    if message is None or message.sender != current_user:
        return make_response(
            jsonify({"message": "Message not found or not from user"}),
            404)

    # update the message
    data = request.get_json()
    message.message = data.get('message')
    message.updated_at = datetime.now()
    message.save()

    # send the updated message back
    return jsonify({"message": "Message updated successfuly"}), 200


@chats_bp.route('/delete/<message_id>', methods=['DELETE'])
@logged_in
def delete(current_user, message_id):
    """ Deletes a message in a chat room """
    # check if user exists and the message is from them
    message = ChatMessage.objects(id=message_id).first()
    if message is None or message.sender != current_user:
        return make_response(
            jsonify({"message": "Message not found or not from user"}),
            404)

    # delete the message
    message.deleted_by.append(current_user)
    message.save()

    # return success message
    return jsonify({"message": "Message deleted successfully"}), 200
