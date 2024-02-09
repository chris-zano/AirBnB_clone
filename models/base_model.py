#!/usr/bin/env python3
"""
This is the base_model.py file
This file contains the BaseModel class
"""


from datetime import datetime
import uuid


class BaseModel:
    """
    This class is the BaseModel class for this application.
    It defines all common attributes and methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Creates a new instance of a model
        :param args: arguments array
        :param kwargs: keyword arguments
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        :return: a string representation of the instance
        """
        return '[{}] ({}) {}'.format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dictionary = self.__dict__
        dictionary.update({'__class__': BaseModel.__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
