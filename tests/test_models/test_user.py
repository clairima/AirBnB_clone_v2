#!/usr/bin/python3
""" test User Class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ test User class """

    def setUp(self):
        """setting up the test cases"""
        self.new = User()

    def test_first_name(self):
        """ test first name """
        self.assertTrue(hasattr(self.new, "first_name"))

    def test_last_name(self):
        """ test last name"""
        self.assertTrue(hasattr(self.new, "last_name"))

    def test_email(self):
        """ test email """
        self.assertTrue(hasattr(self.new, "email"))

    def test_password(self):
        """ test password """
        self.assertTrue(hasattr(self.new, "password"))
