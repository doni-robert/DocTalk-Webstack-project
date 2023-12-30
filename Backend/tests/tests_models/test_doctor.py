#!/usr/bin/env python3
""" Contains the TestDoctorClass class"""
import unittest
from flask import Flask
from db import init_mongodb


class TestDoctorClass(unittest.TestCase):
    """Test the addition and removal of patients belonging to a doctor"""

    def setUp(self):
        """ Sets up a flask app and connects to the db"""
        app = Flask(__name__)
        app.config['DB_HOST'] = 'mongodb://localhost:27017/test_database'
        init_mongodb(app)

    def test_add_doctor_patients(self):
        """Test addition of a patient to a doctor"""
        from models.doctor import Doctor
        from models.patient import Patient

        doctor = Doctor(email="dr_jones@example.com", name="Dr. Jones", password="pass", staff_number=456)
        patient = Patient(email="john_doe@example.com", name="John Doe", password="pass", patient_number=789)
        doctor.save()
        patient.save()

        doctor.add_doctor_patients(patient)
        self.assertIn(patient, doctor.patients)

