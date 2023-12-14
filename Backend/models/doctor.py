#!/usr/bin/env python3
""" The Doctor module"""
from user import User
from patient import Patient
from mongoengine import IntField, ListField, ReferenceField


class Doctor(User):
    """
    The Doctor document that inherits from User
    """
    staff_number = IntField(required=True)
    patients = ListField(ReferenceField(Patient))