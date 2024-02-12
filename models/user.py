#!/usr/bin/python3
"""
This is the user.py module
It contains the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User Class
    Inherits from BaseModel
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
