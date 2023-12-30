#!/usr/bin/env python3
""" Chat message model """

from mongoengine import Document, StringField, ReferenceField, DateTimeField
from models.user import User


class ChatMessage(Document):
    """ Chat message in a chat room """
    message = StringField(required=True)
    sender = ReferenceField(User, required=True)
    receiver = ReferenceField(User, required=True)
    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)
    chat_room = ReferenceField('ChatRoom', required=True)

    meta = {
        'collection': 'chat_messages',
        'indexes': ['sender', 'receiver', 'chat_room'],
        'ordering': ['-created_at']
    }
