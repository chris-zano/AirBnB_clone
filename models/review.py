#!/usr/bin/python3
"""
This is the review.py module
It contains the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review Class
    Inherits from the BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
