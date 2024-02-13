#!/usr/bin/python3
"""
This is the city.py module
It contains the City class for the HBNB project
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    The City Class
    contains
        *ID
        *name
        *state
    """
    state_id = ""
    name = ""
