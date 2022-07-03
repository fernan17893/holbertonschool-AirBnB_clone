#!/usr/bin/python3
"""Test File Storage """

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    ''' this will test the class FileStorage '''

    def test_all(self):
        """tests if all works"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """ Test if new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = '551091'
        user.name = "Fern"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

if __name__ == "__main__":
    unittest.main()
