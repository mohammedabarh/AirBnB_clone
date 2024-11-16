#!/usr/bin/python3
"""This module defines the BaseModel class for the HBnB project."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This class serves as the base model for the HBnB application."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.
        
        Args:
            *args (any): Arguments that are not utilized.
            **kwargs (dict): Key/value attribute pairs to set up the instance.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update the updated_at attribute to the current date and time."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Convert the BaseModel instance to a dictionary.
        
        Returns:
            dict: A dictionary representation of the instance,
                  including the class name under the key __class__.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Provide a string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
