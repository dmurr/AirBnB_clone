#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""
engine
"""

class FileStorage(BaseModel):
    """
    FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return __objects

    def new(self, obj):
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[k] = obj

    def save(self):
        save_dict = {}
        for k,v in type(self).__objects.items():
            v_dict = v.to_dict()
            save_dict[k] = v_dict
        with open(type(self).__file_path, mode='w') as f:
            json.dump(save_dict, f)

    def reload(self):
        with open(__objects) as f:
            return json.load(f)
