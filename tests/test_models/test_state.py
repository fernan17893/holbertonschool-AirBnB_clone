#!/usr/bin/python3
"""Test State"""
import unittest
from models.state import State

class Teststate(unittest.TestCase):
    """Test State"""

    def test_class(self):
    """test class"""
    state1 = State()
    self.assertEqual(state1.__class__.__name__, "State")
