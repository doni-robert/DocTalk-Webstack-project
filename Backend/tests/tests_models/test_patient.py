#!/usr/bin/env python3
""" Contains the TestPatientClass class"""
import unittest
from flask import Flask
from db import init_mongodb


class TestPatientClass(unittest.TestCase):
    """Test the addition and removal of patients belonging to a doctor"""

    def setUp(self):
        """ Sets up a flask app and connects to the db"""
        app = Flask(__name__)
        app.config['DB_HOST'] = 'mongodb://localhost:27017/test_database'
        init_mongodb(app)

    def test_add_patient_doctors(self):
        """ Test the addition of a doctor to a patient's list"""
        from models.doctor import Doctor
        from models.patient import Patient

        doctor = Doctor(email="dr_smiths@example.com", name="Dr. Smith", password="doctorpass", staff_number=123)
        patient = Patient(email="jane_doe@example.com", name="Jane Doe", password="pass", patient_number=79)
        doctor.save()
        patient.save()

        patient.add_patient_doctors(doctor)
        self.assertIn(doctor, patient.doctors)