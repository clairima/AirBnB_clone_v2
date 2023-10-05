#!/usr/bin/python3
""" Test review class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ test Review class """

    def setUp(self):
        """Set up"""
        self.new = Review()

    def test_place_id(self):
        """ test place id """
        self.assertTrue(hasattr(self.new, "place_id"))

    def test_user_id(self):
        """test user id """
        self.assertTrue(hasattr(self.new, "user_id"))

    def test_text(self):
        """ test text """
        self.assertTrue(hasattr(self.new, "text"))
