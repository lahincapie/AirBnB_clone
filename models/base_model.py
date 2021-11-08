#!/usr/bin/python3
""" Base class """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Class: BaseModel """

    def __init__(self, *args, **kwargs):
        """ Constructor Method"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) > 0:
            convert = ["created_at", "updated_at"]
            for key, value in kwargs.items():
                if key in convert:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__"""
        myDict = self.__dict__
        dictStr = {}
        for key, value in myDict.items():
            if isinstance(value, datetime):
                dictStr[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dictStr[key] = value
        dictStr["__class__"] = self.__class__.__name__
        return dictStr

    def __str__(self):
        """ Returns the string form of the class """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ updates the attr updated_at with current datetime """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    @classmethod
    def all(cls):
        """ Prints all instances of the class by the console"""
        return "all {}".format(cls.__name__)

    @classmethod
    def count(cls):
        """ Returns the number of instances of a class """
        return "count {}".format(cls.__name__)

    @classmethod
    def show(cls, __id=''):
        """Returns the string representation of an instance"""
        return "show {} {}".format(cls.__name__, __id)

    @classmethod
    def destroy(cls, _id=''):
        """Destroys an instance"""
        return "destroy {} {}".format(cls.__name__, _id)

    @classmethod
    def update(cls, _id='', attribute_name='', attribute_value=''):
        """Updates an instance"""
        if type(attribute_name) is dict:
            if cls.__name__ + "." + _id in models.storage.all().keys():
                obj = models.storage.all().get('{}.{}'.
                                               format(cls.__name__, _id))
                for key, value in attribute_name.items():
                    setattr(obj, key, value)
                models.storage.save()
                return "\n"
            else:
                return "update {} {}".format(cls.__name__, _id)
        else:
            return "update {} {} {} \"{}\"".\
                format(cls.__name__, _id, attribute_name, attribute_value)
