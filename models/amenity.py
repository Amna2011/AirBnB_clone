#!/usr/bin/python3
from base_model import BaseModel 
class Amenity(BaseModel):
    """my amenity class documentation """
    amenity_name = BaseModel.name()

if __name__ == '__main__':
    Amenity(BaseModel)
