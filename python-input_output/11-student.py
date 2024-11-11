#!/usr/bin/python3
"""
This module defines the Student class.
"""


class Student:
    """
    A class to represent a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with first_name, last_name, age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) 
        and all(isinstance(attr, str) for attr in attrs):
            return {attr: self.__dict__[attr] 
                    for attr in attrs if attr in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
