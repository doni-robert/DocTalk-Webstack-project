#!/usr/bin/env python3
""" The User module"""

from mongoengine import Document, StringField, EmailField, IntField, ListField, ReferenceField


class User(Document):
    """
    The User base model
    """
    email = EmailField(required=True, unique=True)
    name = StringField(max_length=50)
    password = StringField(max_length=255)
    

    meta = {'allow_inheritance': True}

    # Possible methods

    # def create_user():

    # def authenticate_user():

    # def hash_password():

    # def check_password():

    


class Doctor(User):
    """
    The Doctor document that inherits from User
    """
    staff_number = IntField(required=True)
    patients = ListField(ReferenceField('Patient')) #patient set as string to refer to a class defined later

class Patient(User):
    """
    The Patient document that inherits from User
    """
    patient_number = IntField(required=True)
    doctors = ListField(ReferenceField(Doctor))