#!/usr/bin/env python3
"""Chat Module"""

from datetime import datetime
from mongoengine import Document, StringField, ListField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField
from user import User


class Message(EmbeddedDocument):
    """
    The Class embedded document
    """
    sender = ReferenceField(User)
    content = StringField(required=True)
    timestamp = StringField(default=str(datetime.utcnow()))

class Chat(Document):
    """
    The Chat document
    """
    participants = ListField(ReferenceField(User), required=True)
    messages = ListField(EmbeddedDocumentField(Message), default=[])

    # Possible methods

    # def get_chat():

    # def get_chat():

    # def delete_chat():

    # def delete_message():



