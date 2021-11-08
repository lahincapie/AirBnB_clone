#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import pep8
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test cases for FileStorage Class """

    def tearDown(self):
        """Deleting everything at the end"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_pep8_conformance_model_files(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_class(self):
        """ Tests instance of a class """
        storage = FileStorage()
        self.assertTrue(isinstance(storage, FileStorage))

    def test__file_path_exists(self):
        """Tests for the file path existance"""
        storage = FileStorage()
        self.assertTrue(isinstance(storage._FileStorage__file_path, str))

    def test__objects_exists(self):
        """Tests for the objects existance"""
        storage = FileStorage()
        self.assertTrue(isinstance(storage._FileStorage__objects, dict))

    def test_all(self):
        """Tests all() function"""
        storage = FileStorage()
        dict_all = storage.all()
        self.assertTrue(isinstance(dict_all, dict))

    def test_new(self):
        """Tests new() function"""
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        self.assertNotEqual(storage.all(), 0)

    def test_save(self):
        """Tests save() function"""
        obj = BaseModel()
        obj.name = "Kotlin"
        storage = FileStorage()
        obj.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            dict_json = json.load(f)
        value_dict = dict_json.get("BaseModel.{}".format(obj.id))
        self.assertEqual(value_dict['name'], "Kotlin")

    def test_reload(self):
        """Tests reload() function"""
        obj = BaseModel()
        storage = FileStorage()
        obj.name = "Plakton"
        obj.age = 88.32
        obj.save()
        storage._FIleStorage__objects = {}
        storage.reload()
        self.assertNotEqual(storage.all(), {})
