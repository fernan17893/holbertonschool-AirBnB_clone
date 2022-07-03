#!/usr/bin/python3
"""Test Review"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review

class Testreview(unittest.TestCase):

    def test_class(self):
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")
