#!/usr/bin/env python3
""" Chat message model """

from mongoengine import Document, StringField, ReferenceField, DateTimeField
from datetime import datetime
from models.user import User


class ChatMessage(Document):
    """ Chat message in a chat room """
    message = StringField(required=True)
    sender = ReferenceField(User, required=True)
    receiver = ReferenceField(User, required=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    chat_room = ReferenceField('ChatRoom', required=True)

    meta = {
        'collection': 'chat_messages',
        'indexes': ['sender', 'receiver', 'chat_room'],
        'ordering': ['-created_at']
    }

    @staticmethod
    def create_message(message, sender, receiver, chat_room):
        """ Creates a new message """
        new_message = ChatMessage(
            message=message,
            sender=sender,
            receiver=receiver,
            chat_room=chat_room
        )
        new_message.save()

        return new_message

    @staticmethod
    def get_messages_by_room(room_name):
        """ Gets all messages from a chat room """
        messages = ChatMessage.objects(chat_room=room_name)

        return messages
