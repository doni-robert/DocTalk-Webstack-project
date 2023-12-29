#!/usr/bin/env python3
""" Chat room model """

from mongoengine import (
    Document,
    StringField,
    ReferenceField,
    ListField,
    DateTimeField
)
from datetime import datetime
from models.user import User


class ChatRoom(Document):
    """ Chat room in the database """
    room_name = StringField(max_length=50, required=True, unique=True)
    users = ListField(ReferenceField(User))
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    meta = {
        'collection': 'chat_rooms',
        'indexes': ['room_name'],
        'ordering': ['-created_at']
    }

    @staticmethod
    def create_room(room_name, user):
        """ Creates a new chat room """
        new_room = ChatRoom(room_name=room_name, users=[user])
        new_room.save()

        return new_room

    @staticmethod
    def get_room_by_name(room_name):
        """ Retrieves a chat room based on a name """
        if room_name:
            room = ChatRoom.objects(room_name=room_name).first()

            return room
        return None

    @staticmethod
    def get_user_by_name(username):
        """ Retrieves a user based on a name """
        if username:
            user = User.objects(username=username).first()

            return user
        return None
