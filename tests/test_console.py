#!/usr/bin/python3
"""Unittesting console.py"""
from console import HBNBCommand
from io import StringIO
import models
from models.engine.file_storage import FileStorage
import os
import unittest

from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """Unittesting for the command interpreter"""

    @classmethod
    def setUpClass(cls):
        """
        rename file.json -> tempFile.json
        """
        try:
            os.rename("file.json", "tempFile.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """
        rename tempFile.json -> file.json
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

        try:
            os.rename("tempFile.json", "file.json")
        except Exception:
            pass

    def setUp(self):
        """setting up test case"""
        self.HBNB = HBNBCommand()

    def test_create(self):
        """Test create command (basic method)"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            bm = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all BaseModel")
            self.assertIn(bm, f.getvalue())

    def test_create_parameters(self):
        """Test create <name>=<value>"""
        with patch("sys.stdout", new=StringIO()) as f:
            call = ('create Place city_id="0001" \
                    user_id="0001" name="My_little_house" number_rooms=4 \
                    number_bathrooms=2 max_guest=10 price_by_night=300 \
                    latitude=37.773972 longitude=-122.431297')
            self.HBNB.onecmd(call)
            pl = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            output = f.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'name': 'My little house'", output)
            self.assertIn("'number_rooms': 4", output)
            self.assertIn("'number_bathrooms': 2", output)
            self.assertIn("'max_guest': 10", output)
            self.assertIn("'latitude': 37.773972", output)
            self.assertIn("'price_by_night': 300", output)
            self.assertIn("'longitude': -122.431297", output)
