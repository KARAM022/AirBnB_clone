#!/usr/bin/python3
"""FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serialize instances to a JSON file
    and deserialize JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the 'obj' with key '<obj class name>.id'"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file"""
        objects_dict = {}
        for key, obj in FileStorage.__objects.items():
            objects_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file to '__objects'"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'User':
                        self.__objects[key] = User.from_dict(value)
                    else:
                        class_ = globals()[class_name]
                        self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
