#!/usr/bin/python3
""" Defines the basemodel classs"""
import models
import uuid
from datetime import datetime

class BaseModel:
    """A class BaseModel that defines all common attributes/methods for other classes."""
    def __init__(self, **kwargs):
        """Initialize instance attributes."""
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.today()

    def __str__(self):
        """Return a string representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return a dictionary representation."""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        
        # Add error handling for missing keys
        for key in ["created_at", "updated_at"]:
            if key in instance_dict:
                instance_dict[key] = instance_dict[key].isoformat()

        return instance_dict
