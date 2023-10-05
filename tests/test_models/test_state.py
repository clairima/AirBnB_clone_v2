#!/usr/bin/python3
""" Test State class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ test state class"""

    def setUp(self):
        """setting up the test cases"""
        self.new = State()

    def test_name3(self):
        """ test name"""
        self.assertTrue(hasattr(self.new, "name"))
