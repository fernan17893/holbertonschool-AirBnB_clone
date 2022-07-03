#!/usr/bin/python3
"""Module to define user class"""


from models.base_model import BaseModel

class User(BaseModel):
    """Definition of user class"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Method called on initialization of new user"""
        super().__init__()
