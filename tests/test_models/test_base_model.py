#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models import storage
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test cases for BaseModel Class """

    def test_class(self):
        """ Tests instance of a class """
        base = BaseModel()
        self.assertTrue(isinstance(base, BaseModel))

    def test_id(self):
        """ Tests that ids are unique """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertTrue(base1.id != base2.id)

    def test_kwargs(self):
        """ Tests instanciation with kwargs"""
        base = BaseModel()
        base.name = "Dani"
        dicty = base.to_dict()
        self.assertTrue("name" in dicty)

    def test_to_dict(self):
        """ Tests that the function retrieves a dictionary """
        base = BaseModel()
        ret_dict = base.to_dict()
        self.assertTrue(isinstance(ret_dict, dict))

    def test_str(self):
        """ Tests the str repr. of an object """
        base = BaseModel()
        base_str = base.__str__()
        self.assertTrue(isinstance(base_str, str))

    def test_save(self):
        """ Tests the save method """
        obj = BaseModel()
        time1 = obj.updated_at
        obj.name = "Plankton"
        obj.age = 88.32
        obj.save()
        time2 = obj.updated_at
        dict_obj = storage.all()
        obj_ref = storage.all().get("BaseModel.{}".format(obj.id))
        self.assertNotEqual(time1, time2)
        self.assertEqual(obj.id, obj_ref.id)
        self.assertEqual(obj.name, obj_ref.name)
        self.assertEqual(obj.age, obj_ref.age)
        self.assertTrue(os.path.exists('file.json'))
