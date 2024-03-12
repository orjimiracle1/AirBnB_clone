#!/usr/bin/python3
"""
    Defines a User class.
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    Class represents a user object.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
