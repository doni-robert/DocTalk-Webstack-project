#!/usr/bin/env python3
""" The Doctor module"""
from models.user import User
from mongoengine import IntField, ListField, ReferenceField


class Doctor(User):
    """
    The Doctor document that inherits from User
    """

    staff_number = IntField(required=True)
    patients = ListField(ReferenceField('Patient'))


    def get_patients(self):
        """Retrieves a list of a doctor's patients"""
        return self.patients
    
    def add_doctor_patients(self, patient):
        """Adds a patient to the list of a doctor's patients """
        from models.patient import Patient

        if patient in Patient.objects().all():
            self.patients.append(patient)
        else:
            return None
        
    def remove_doctor_patients(self, patient):
        """Remove a patient from the list of a doctor's patients """
        if patient in self.patients:
            self.patients.remove(patient)
        else:
            return None