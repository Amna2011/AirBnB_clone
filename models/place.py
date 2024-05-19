#!/usr/bin/python3
from base_model import BaseModel
from city import City
from amenity import Amenity
from user import User


class Place(BaseModel):
    """my place class documentation """
    self.city_id = City.id()
    self.user_id = User.id
    self.place_name = BaseModel.name()
    self.description = ""
    self.number_rooms = 0
    self.number_bathrooms = 0
    self.max_guest = 0
    self.price_by_night = 0
    self.latitude = 0.0
    self.longitude = 0.0
    self.amenity_ids = Amenity.id


if __name__ == '__main__':
    Place(BaseModel)
