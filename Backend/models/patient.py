#!/usr/bin/env python3
""" The Patient module"""
from user import User
from doctor import Doctor
from mongoengine import IntField, ListField, ReferenceField


class Patient(User):
    """
    The Patient document that inherits from User
    """
    patient_number = IntField(required=True)
    doctors = ListField(ReferenceField(Doctor))