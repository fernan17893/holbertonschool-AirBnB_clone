#!/usr/bin/python3
"""Unit tests for Base_Model"""


import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Unit tests for task 1"""
    def test_created_at(self):
        """Test that simple base model can be created"""
        b1 = BaseModel()
        self.assertEqual(b1.__class__.__name__, "BaseModel")

if __name__ == "__main__":
    unittest.main()
