#!/usr/bin/env python3
" Class FileStorage which serializes instances to JSON file and vice versa"
import json
import models
from models.base_model import BaseModel

class FileStorage:
    """ Class File Storage """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with the key obj.__class__.__name__ """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ seriealizes __objects to the JSON file path """
        new_dic = {}
        with open(self.__file_path, mode="w", encoding='UTF-8') as json_file:
            for k, v in self.__objects.items():
                new_dic[k] = v.to_dict()
            json_file.write(json.dumps(new_dic))

    def reload(self):
        """ desrializes the JSON file to _objects, if the file doesnt exist no exception should be raised """
        try:
            with open(self.__file_path, mode="r", encoding='UTF-8') as f:
                for o in json.load(file).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
