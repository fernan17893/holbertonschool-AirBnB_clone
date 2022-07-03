#!/usr/bin/python3
"""Module to define user class"""


from models.base_model import BaseModel

class User(BaseModel):
    """Definition of user class"""

    def __init__(self, email='', password='', first_name='', last_name=''):
        """Method called on initialization of new user"""
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        super().__init__()
