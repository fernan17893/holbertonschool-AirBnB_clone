#!/usr/bin/python3
"""Unit tests for Base_Model"""


import unittest
from models.base_model import BaseModel


class Test_3(unittest.TestCase):
    """Unit tests for task 1"""
    def test_BaseModel_creation(self):
        """Test that simple base model can be created"""
        b1 = BaseModel()
        self.assertAlmostEqual(1, 1)
