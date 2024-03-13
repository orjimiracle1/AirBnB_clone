#!/usr/bin/python3
"""Defines a persistance FileStorage class object."""
import json
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place

class FileStorage:
    """
    Class represents an abstracted persistence storage engine
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """
        Returns __objects(dictionary)
        """
        return FileStorage.__objects

    def save(self):
        """
        Serialize __objects to the JSON file __file_path.
        """
        obj_dict = FileStorage.__objects
        objsdict = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objsdict, f)

    def new(self, obj):
        """
        set prefix key <obj_class_name>.id to each 
            obj dictionary
        """
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def reload(self):
        """
        Deserialize the JSON file __file_path
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for value in objdict.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
