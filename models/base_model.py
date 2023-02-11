#!/usr/bin/python3
"""
This is the parent class (called BaseModel) used to take care\
of the initialization of your future instances
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class: defines all common\
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        A class Constructor for the Id, created_at and updated_at
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.\
                            strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """
        Should print string method
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates The Attribute: (update_at) , with the curent datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns A Dictionary containg all keys/values of __dict__ instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return (new_dict)
