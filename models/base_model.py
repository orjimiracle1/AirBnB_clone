#!/usr/bin/python3
"""This script is the base model"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if bool(kwargs):
            date_format =  "%Y-%m-%dT%H:%M:%S.%f"
            for key,value in kwargs.items():
                if key == "__class__":
                    continue
                if (key == "created_at" or key == "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """Returns official string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
