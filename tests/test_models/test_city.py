#!/usr/bin/python3
""" Test City"""

import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review

class Testcity(unittest.TestCase):
    """ Test for city """

    def test_class(self):
        """test class"""
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")
