#!/usr/bin/env python3
""" Base Model that defines all common attributes/methods for other classes """
from datetime import datetime
import time
import uuid

class BaseModel:
    """ Class BaseModel """

    def __init__(self, *args, **kwargs):
        """ Public instance attribute assings uuid when an instance is created """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items:
                if k != __class__:
                    setattr(self, k, v)                

    def __str__(self):
        """ prints """
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """ updates updated_at with current datetime """
        return (self.updated_at == datetime.now())

    def to_dict(self):
        """ Returns disctionary representation of BaseModel """
        dic = self.__dict__.copy()
        dic[__class__] = self.name
        dic[self.created_at] = self.created_at.isoformat()
        dic[self.updated_at] = self.updated_at.isoformat()
        return (dic)
       