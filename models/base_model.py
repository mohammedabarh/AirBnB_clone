#!/usr/bin/python3
"""
This module implements the foundation class BaseModel
that other classes will inherit from
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class that defines common attributes and methods
    for other classes in the project
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize new instance of BaseModel
        Args:
            *args: Variable length argument list (not used)
            **kwargs: Arbitrary keyword arguments for instance attributes
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
        """
        Updates the public instance attribute updated_at
        with current timestamp
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Creates dictionary representation of instance
        Returns:
            dict: Contains all keys/values of __dict__ of the instance,
                 created_at and updated_at in ISO format,
                 and class name in __class__ key
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """
        Returns string representation of BaseModel instance
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
