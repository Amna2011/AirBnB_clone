#!/usr/bin/python3
from base_model import BaseModel
from city import City
from amenity import Amenity
from user import User
class Place(BaseModel):
    """my place class documentation """
    city_id = City.id()
    user_id = User.id
    place_name = BaseModel.name()
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = Amenity.id


if __name__ == '__main__':
    Place(BaseModel)
