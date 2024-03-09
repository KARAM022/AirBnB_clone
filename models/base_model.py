#!/usr/bin/python3
"""BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self,
                                key,
                                datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            from models.engine import storage
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """update 'updated_at' with the current datetime"""
        from models.engine import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        var_dict = self.__dict__.copy()
        var_dict['__class__'] = self.__class__.__name__
        var_dict['created_at'] = self.created_at.isoformat()
        var_dict['updated_at'] = self.updated_at.isoformat()
        return var_dict
