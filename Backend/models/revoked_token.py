#!/usr/bin/env python3
""" The TokenBlockList module"""
from mongoengine import Document, StringField, EmailField

class TokenBlockList(Document):
    """ The TokenBlockList model """
    jti = StringField(unique=True)

    @staticmethod
    def is_token_blacklisted(jti):
        # Check if the token JTI is in the blocklist stored in MongoDB
        return TokenBlockList.objects(jti=jti).first() is not None
    
    @staticmethod
    def add_token_to_blocklist(jti):
        """ Creates and saves blocked token"""
        blocked_token = TokenBlockList(jti=jti).save()
        return blocked_token