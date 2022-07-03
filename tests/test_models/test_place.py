#!/usr/bin/python3
"""Test Place"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testplace(unittest.TestCase):


    def test_class(self):
        place1 = Place()
        self.assertEqual(place1.__class__.__name__, "Place")
