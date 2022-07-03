#!/usr/bin/python3
"""Module to define class"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Definition of class"""

    name = ''

    def __init__(self, *args, **kwargs):
        """Method called on initialization of new object"""
        super().__init__()
