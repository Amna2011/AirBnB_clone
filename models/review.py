#!/usr/bin/python3
from base_model import BaseModel
from place import Place
from user import User
class Review(BaseModel):
    """my review class documentation """
    place_id = Place.id
    user_id = User.id
    text = ""


if __name__ == '__main__':
    Review(BaseModel)
