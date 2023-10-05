#!/usr/bin/python3
""" testing Amenity"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ testing amenity class """

    def setUp(self):
        self.new = Amenity()

    def test_name2(self):
        """ test name2"""
        self.assertTrue(hasattr(self.new, "name"))
