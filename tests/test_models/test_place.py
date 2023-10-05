#!/usr/bin/python3
""" Test Place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Testing place class"""

    def setUp(self):
        """Setting up the test cases"""
        self.new = Place()

    def test_city_id(self):
        """ test city_id"""
        self.assertTrue(hasattr(self.new, "city_id"))

    def test_user_id(self):
        """ test user_id"""
        self.assertTrue(hasattr(self.new, "user_id"))

    def test_name(self):
        """ test name"""
        self.assertTrue(hasattr(self.new, "name"))

    def test_description(self):
        """ test description"""
        self.assertTrue(hasattr(self.new, "description"))

    def test_number_rooms(self):
        """ test the number of rooms"""
        self.assertTrue(hasattr(self.new, "number_rooms"))

    def test_number_bathrooms(self):
        """ test the number of bathrooms"""
        self.assertTrue(hasattr(self.new, "number_bathrooms"))

    def test_max_guest(self):
        """ test the max guests"""
        self.assertTrue(hasattr(self.new, "max_guest"))

    def test_price_by_night(self):
        """ test price by night"""
        self.assertTrue(hasattr(self.new, "name"))

    def test_latitude(self):
        """ test latitude"""
        self.assertTrue(hasattr(self.new, "latitude"))

    def test_longitude(self):
        """ test longitude"""
        self.assertTrue(hasattr(self.new, "longitude"))

    def test_amenity_ids(self):
        """ test amenity ids"""
        self.assertTrue(hasattr(self.new, "amenity_ids"))
