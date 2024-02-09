#!/usr/bin/python3
"""
This is file_storage.py file
this file contains the FileStorage class
"""


import json
from os import path


class FileStorage:
    """
    serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects.update({obj.to_dict()['__class__'] + '.' + obj.id: str(obj)})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.loads(f.read())
        except IOError:
            pass
