#!/usr/bin/python3
#import models.base_model.BaseModel
from base_model import BaseModel 
class User(BaseModel):
    """my class user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    new_user = BaseModel()
    print(new_user.id)
    new_user.save_update()

if __name__ == '__main__':
    User(BaseModel)
