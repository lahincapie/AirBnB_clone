#!/usr/bin/python3
""" FileStorage class """
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ Class: FileStorage """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key """
        key = obj.__class__.__name__ + '.' + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        savedict = {}
        for key, value in FileStorage.__objects.items():
            savedict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(savedict))

    def reload(self):
        """deserializes the JSON file to __objects"""
        dictReload = {}
        try:
            cls_arr = {"BaseModel": BaseModel, "Amenity": Amenity,
                       "City": City, "Place": Place,
                       "Review": Review, "State": State, "User": User}
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                dictReload = json.load(file)
                for key, value in dictReload.items():
                    cls_to_ins = cls_arr.get(value['__class__'])
                    obj = cls_to_ins(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
