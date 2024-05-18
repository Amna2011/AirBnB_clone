#!/usr/bin/python3
from base_model import BaseModel
from state import State
class City(BaseModel):
    """my city class documentation """
    city_name = BaseModel.name()
    city_id = State.id()

if __name__ == '__main__':
    City(BaseModel)
