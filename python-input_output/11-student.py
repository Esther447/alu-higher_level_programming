#!/usr/bin/python3
"""
This module defines the Student class.

The Student class represents a student with attributes for first name, last name, and age.
It provides methods for converting an instance to a dictionary representation (useful for JSON
serialization) and for updating attributes from a dictionary (deserialization).
"""

class Student:
    """
    A class to represent a student.

    Attributes:
    -----------
    first_name : str
        The first name of the student.
    last_name : str
        The last name of the student.
    age : int
        The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with first_name, last_name, and age.

        Parameters:
        -----------
        first_name : str
            The first name of the student.
        last_name : str
            The last name of the student.
        age : int
            The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Parameters:
        -----------
        attrs : list, optional
            A list of attribute names to include in the dictionary (default is None).

        Returns:
        --------
        dict
            A dictionary representation of the Student instance.
            If attrs is a list of strings, only attributes listed in attrs are included.
            Otherwise, all attributes are included.
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: self.__dict__[attr] for attr in attrs if attr in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.

        Parameters:
        -----------
        json : dict
            A dictionary where each key is an attribute name, and each value is
            the new value for the attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)
