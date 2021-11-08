#!/usr/bin/python3
""" User class """
import models


class User(models.base_model.BaseModel):
    """ Class: User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
