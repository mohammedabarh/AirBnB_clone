#!/usr/bin/python3
"""
This module implements the FileStorage class for handling
persistent data storage and retrieval
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
    Manages serialization and deserialization of objects to/from JSON file
    
    Private Class Attributes:
        __file_path: String path to JSON file for data persistence
        __objects: Dictionary storing all objects by <class_name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all stored objects
        
        Returns:
            Dictionary containing all stored objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds new object to storage dictionary
        
        Args:
            obj: Instance to be stored in __objects
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Persists current state of __objects to JSON file
        Converts all objects to dictionary representation before saving
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        Restores objects from JSON file to __objects
        Creates appropriate object instances based on class name
        Silently fails if file doesn't exist
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
