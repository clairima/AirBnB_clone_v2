#!/usr/bin/python3
""" Testing city class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ testing City class"""

    def test_state_id(self):
        """ testing state id"""
        new = City()
        self.assertTrue(hasattr(new, "state_id"))

    def test_name(self):
        """ testing name"""
        new = City()
        self.assertTrue(hasattr(new, "name"))
