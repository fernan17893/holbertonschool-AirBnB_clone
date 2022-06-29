#!/usr/bin/env python3
" Class FileStorage which serializes instances to JSON file and vice versa"
import json
from models.base_model import BaseModel


class FileStorage:
    """ Class File Storage """

    _file_path = file.json
    _objects = {}

    def all(self):
    """ returns the dictionary """
    return self._objects

    def new(self, obj):
    # sets in _objects the obj with key
    self._objects = obj.__self.id

    def save(self):
    # serializes objects to JSON file path
    

    def reload(self):
    # desrializes the JSON file to _objects
