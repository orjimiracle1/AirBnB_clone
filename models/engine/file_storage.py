#!/usr/bin/python3
""" File storage handles persistence """
import json

class FileStorage:
    """
       FileStorage that serializes instances 
       to a JSON file and deserializes JSON file to instances 
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_name}.{obj.id}"] = obj
    
    def save(self):
        """Serialize __objects to the JSON file __file_path"""
        dict_obj = FileStorage.__objects
        fn_dict = {key: value.to_dict for key,value in dict_obj.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(fn_dict, f)
    
    def reload(self):
        """Deserialize the JSON file 
            __file_path to __objects, if it exists.
        """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)

            for values in obj_dict.values():
                class_name = values["__class__"]
                del values["__class__"]
                self.new(eval(class_name)(**values))
        except FileNotFoundError:
            return