"""Defines the data file storage"""

import json
import os
import uuid
from datetime import datetime

class FileStorage():
    """_summary_
        Filestorage class serializes and deserializes json data to file and vice versa
        Args:

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """_summary_
            returns the dictionary __objects
        Returns:
            _type_: Class attribute 
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """_summary_
            sets in __objects the obj with key <obj class name>.id
        Args:
            obj (_type_): _description_
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ Serialize object to json format"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            all_dict = {key: obj.to_dict() for key, obj in 
                        FileStorage.__objects.items()}
            json.dump(all_dict, f)

    def reload(self):
        """Reload file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key,value in data.items():
                    FileStorage.__objects[key] = eval(value["__class__"](**value))
    