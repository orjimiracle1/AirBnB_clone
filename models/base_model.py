#!/usr/bin/python3
""" Defines the basemodel classs"""
import uuid
from datetime import datetime
class BaseModel:
    """
        BaseModel class holds all common attributes/
        methods for other classes 
    """
    def __init__(self, **kwargs):
        """Instane contructor"""
        tfmt = "%Y-%m-%dT%H:%M:%S.%f"
        if bool(kwargs):
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tfmt)
                else:
                    self.__dict__[key] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self) -> str:
        """String reprsentation of class declaration"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at 
            with the current datetime 
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values """
        all_dict = self.__dict__.copy()
        all_dict["__class__"] = self.__class__.__name__
        all_dict["created_at"] = self.created_at.isoformat()
        all_dict["updated_at"] = self.updated_at.isoformat()
        return all_dict