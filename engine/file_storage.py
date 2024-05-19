#!/usr/bin/python3
class FileStorage:
    """ My FileStorage class documentation """
    __file_path = ""
    __objects = {}
    def all(self):
        """my function that returns all my objects"""
        return __objects
    def new(self, obj):

