#!/usr/bin/env python3
""" Chat room model """

from mongoengine import (
    Document,
    StringField,
    ReferenceField,
    DateTimeField,
    ListField
)
from models.user import User


class ChatRoom(Document):
    """ Chat room in the database """

    name = StringField(required=True)
    users = ListField(ReferenceField('User'), required=True)
    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)
    messages = ListField(ReferenceField('ChatMessage'))

    meta = {
        'collection': 'chat_rooms',
        'indexes': ['name'],
        'ordering': ['-created_at']
    }
