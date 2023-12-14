#!/usr/bin/env python3
""" The User module"""
from mongoengine import Document, StringField, EmailField

class User(Document):
    """
    The User base model
    """
    email = EmailField(required=True, unique=True)
    name = StringField(max_length=50)
    password = StringField(max_length=255)
    

    meta = {'allow_inheritance': True}


    @staticmethod
    def is_authenticated():
        """ Checks whether a user is authenticated"""
        return True

    @staticmethod
    def is_active():
        """ Checks whether a user is active """
        return True
    
    def get_user_by_email(email):
        """ Retrieves a user based on an email"""
        if email:
            user = User.objects(email=email).first()

            return user
        
    def save_user(email, name, password):
        """ Adds a new user to the database """
        new_user = User(email=email, name=name, password=password)
        new_user.save()

        return new_user
    
    def get_contacts(self):
        """ Retrieves the relevant contacts for a user"""
        from models.doctor import Doctor
        from models.patient import Patient

        if isinstance(self, Doctor):
            return self.patients
        
        if isinstance(self, Patient):
            return self.doctors




    # Possible methods

    # def create_user():

    # def authenticate_user():

    # def hash_password():

    # def check_password():

