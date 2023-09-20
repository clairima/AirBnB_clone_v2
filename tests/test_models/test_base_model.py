#!/usr/bin/python3
""" test BaseModel class"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ testing BaseModel class"""

    def __init__(self, *args, **kwargs):
        """ a constructor method"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    @classmethod
    def setUpClass(cls):
        """
        rename file.json -> tempFile.json
        """
        try:
            os.rename("file.json", "tempFile.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()

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
        del cls.storage

    def test_default(self):
        """ default test"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ test init with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ test wrong values"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)

    def test_str(self):
        """ test if string value"""
        i = self.value()
        dict = i.to_dict()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """test todict method """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ test the none case of kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ test id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ test created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ test updated at attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
