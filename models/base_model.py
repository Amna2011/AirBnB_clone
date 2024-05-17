#!/usr/bin/python3
import cmd
from uuid import uuid4
from datetime import datetime
class MyConsole(cmd.Cmd):
    """ My MyConsole class """
    prompt = "(hbnb) "

class BaseModel:
    """ My BaseModel class """
    def __init__(self, *args, **kwargs):
        """ assign a few common default attributes to all instance of this class """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        #self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.created_at = self.created_at.isoformat()
        if args:
            for values in args:
                print(values)
        """loop and access all the key-value paired values parsed into kwargs """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"
    def save_update(self):
        """update updated_at attribute with the current date and time """
        #from yourPackage import storage
        updated_at = datetime.now()
        #storage.save()

        """self.updated_at = self.updated_at.isoformat() """
    def to_dict(self):
        dictFormat = {}
        """add a class key to identify the class name of the instance attribute"""
        dictFormat["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            """get the values which are of datetime object type """
            if isinstance(val, datetime):
                """convert them to string objects in ISO format """
                dictFormat[key] = val.isoformat()
            else:
                dictFormat[key] = val
        return dictFormat
