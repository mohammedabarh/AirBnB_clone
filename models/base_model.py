#!/usr/bin/python3
"""Base model module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """String representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save the instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance to dictionary"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
