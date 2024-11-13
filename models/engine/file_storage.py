#!/usr/bin/python3
"""FileStorage Module"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes JSON file to __objects"""
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name = value["__class__"]
                        obj = classes[class_name](**value)
                        self.new(obj)
        except Exception:
            pass
