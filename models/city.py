#!/usr/bin/python3
"""Module to define class"""


from models.base_model import BaseModel


class City(BaseModel):
    """Definition of class"""

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """Method called on initialization of new object"""
        super().__init__()
