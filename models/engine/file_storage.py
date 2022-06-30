#!/usr/bin/env python3
" Class FileStorage which serializes instances to JSON file and vice versa"
import json
from models.base_model import BaseModel


class FileStorage:
    """ Class File Storage """

    _file_path = "file.json"
    _objects = {}

    def all(self):
    """ returns the dictionary """
    return self.__objects

    def new(self, obj):
    # sets in _objects the obj with key
    key = obj.__class__.__name__ + "." + obj.id
    self.__objects[key] = obj

    def save(self):
    # serializes objects to JSON file path
     new_dic = {}
        with open(self.__file_path, mode="w", encoding='UTF-8') as f:
            for k, v in self.__objects.items():
                new_dic[k] = v.to_dict()
            json.dump(new_dic, f)

    def reload(self):
    # desrializes the JSON file to _objects
    if path.isfile(self.__file_path):
        with open(slf.__file_path, mode="r", encoding 'UTF-8') as f:
            for k, v in (json.load(f)).items():
                v = eval(v["__class__"])(**v)
                 self.__objects[k] = v
