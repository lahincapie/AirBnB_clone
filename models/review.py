#!/usr/bin/python3
""" Review class """
import models


class Review(models.base_model.BaseModel):
    """ Class: Review"""
    place_id = ""
    user_id = ""
    text = ""
