#!/usr/bin/python3
"""Defines Review class object."""
from models.base_model import BaseModel

class Review(BaseModel):
    """
        A review class object that
            represents review
    """
    place_id = ""
    user_id = ""
    text = ""
