#!/usr/bin/env python3
""" Handle chat rooms requests and responses """

from flask import request, jsonify
from models.chat_room import ChatRoom


def create_room():
    """
    create a new chat room

    Returns:
        json: new room or error message
    """
    try:
        new_room = ChatRoom(users=[request.json.get('sender_id'),
                                   request.json.get('receiver_id')])
        new_room.save()
        return jsonify(new_room.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 409


def get_rooms(user_id):
    """
    get chat rooms for a specific user

    Args:
        user_id (str): user id

    Returns:
        json: list of rooms or error message
    """
    try:
        rooms = ChatRoom.objects(users__in=[user_id])
        return jsonify([room.to_dict() for room in rooms]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


def get_chat_rooms(first_user_id, second_user_id):
    """
    get chat rooms of two specific user

    Args:
        first_user_id (str): first user id
        second_user_id (str): second user id

    Returns:
        json: list of rooms or error message
    """
    try:
        rooms = ChatRoom.objects(users__all=[first_user_id, second_user_id])
        return jsonify([room.to_dict() for room in rooms]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


def get_room(room_id):
    """
    get a specific chat room

    Args:
        room_id (str): room id

    Returns:
        json: room or error message
    """
    try:
        room = ChatRoom.objects.get(id=room_id)
        return jsonify(room.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


def delete_room(room_id):
    """
    delete a chat room

    Args:
        room_id (str): room id

    Returns:
        json: success or error message
    """
    try:
        room = ChatRoom.objects.get(id=room_id)
        room.delete()
        return jsonify({"message": "room deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


def update_room(room_id):
    """
    edit a chat room

    Args:
        room_id (str): room id

    Returns:
        json: success or error message
    """
    try:
        room = ChatRoom.objects.get(id=room_id)
        room.update(**request.get_json())
        return jsonify({"message": "room updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


def add_user(room_id, user_id):
    """
    add a user to a chat room

    Args:
        room_id (str): room id
        user_id (str): user id

    Returns:
        json: success or error message
    """
    try:
        room = ChatRoom.objects.get(id=room_id)
        room.update(push__users=user_id)
        return jsonify({"message": "user added"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


def remove_user(room_id, user_id):
    """
    remove a user from a chat room

    Args:
        room_id (str): room id
        user_id (str): user id

    Returns:
        json: success or error message
    """
    try:
        room = ChatRoom.objects.get(id=room_id)
        room.update(pull__users=user_id)
        return jsonify({"message": "user removed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404
