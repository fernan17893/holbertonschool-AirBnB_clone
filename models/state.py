#!/usr/bin/python3
"""Module to define State class"""


from models.base_model import BaseModel


class State(BaseModel):
    """Definition of State class"""

    name = ''

    def __init__(self, *args, **kwargs):
        """Method called on initialization of new user"""
        super().__init__()
