#!/usr/bin/env python3
""" Handle chat messages requests and responses """

from flask import request, jsonify
from models.chat_message import ChatMessage


def create_message():
    """
    Create a new message

    Returns:
        json: new message or error message
    """
    try:
        new_message = ChatMessage(**request.get_json())
        new_message.save()
        return jsonify(new_message.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def get_messages(chat_room_id):
    """
    get messages for a specific chat room

    Args:
        chat_room_id (str): chat room id

    Returns:
        json: list of messages or error message
    """
    try:
        messages = ChatMessage.objects(chat_room_id=chat_room_id)
        return jsonify([message.to_dict() for message in messages]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def delete_message(message_id):
    """
    delete a message

    Args:
        message_id (str): message id

    Returns:
        json: success or error message
    """
    try:
        message = ChatMessage.objects.get(id=message_id)
        message.delete()
        return jsonify({"message": "message deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def update_message(message_id):
    """
    edit a message

    Args:
        message_id (str): message id

    Returns:
        json: success or error message
    """
    try:
        message = ChatMessage.objects.get(id=message_id)
        message.update(**request.get_json())
        return jsonify({"message": "message updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
