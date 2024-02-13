#!/usr/bin/python3
"""
This is file_storage.py file
this file contains the FileStorage class
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary of models in storage
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects obj with key <obj_class_name>.id
        """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the JSON file __file_path.
        """
        obj_dict = FileStorage.__objects
        val = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(val, f)

    def reload(self):
        """
        Deserialize the JSON file __file_path to __objects, if it exists.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
