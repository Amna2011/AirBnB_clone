#!/usr/bin/python3
from base_model import BaseModel


class State(BaseModel):
    """my state class documentation """
    self state_name = BaseModel.name()
    self.state_name = ""


if __name__ == '__main__':
    State(BaseModel)
