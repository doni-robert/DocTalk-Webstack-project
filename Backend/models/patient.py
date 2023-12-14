#!/usr/bin/env python3
""" The Patient module"""
from models.user import User
from mongoengine import IntField, ListField, ReferenceField


class Patient(User):
    """
    The Patient document that inherits from User
    """

    patient_number = IntField(required=True)
    doctors = ListField(ReferenceField('Doctor'))


    def get_patient_doctors(self):
        """Retrieves a list of a patient's doctors"""
        return self.doctors
    
    def add_patient_doctors(self, doctor):
        """Adds a doctor to the list of a patient's doctors """
        from models.doctor import Doctor

        if doctor in Doctor.objects().all():
            self.doctors.append(doctor)
        else:
            return None
        
    def remove_patient_doctors(self, doctor):
        """Remove a doctor from the list of a patient's doctors """
        if doctor in self.patients:
            self.doctors.remove(doctor)
        else:
            return None
        
