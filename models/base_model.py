#!/usr/bin/python3
"""The BaseModel class object."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """BaseModel class holds all common attributes
        of objects in the project
    """


    def __init__(self, *args, **kwargs):
        """
            Initialize BaseModel.
        """
        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if bool(kwargs):
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_fmt)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def to_dict(self):
        """
        Converts and returns object as dictionary
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def save(self):
        """Update updated_at"""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """String representation of the BaseModel instance object."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
