#!/usr/bin/python3
""" Test State class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ test state class"""

    def __init__(self, *args, **kwargs):
        """ a constructor method """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
