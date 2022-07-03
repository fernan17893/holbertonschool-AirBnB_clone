#!/usr/bin/python3
"""Module to define class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Definition of class"""

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """Method called on initialization of new object"""
        super().__init__()
