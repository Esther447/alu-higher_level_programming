#!/usr/bin/python3
"""
Module for the Student class.
"""


class student:
    """
    A class to represent a student.
    """


    def __init__(self, first_name, last_name, age):
        """
        Initializes the student intance with first_name, last_name, age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the student instance.
        """

        if attrs is None:
            return self.__dict__


    def reload_from_json(self, json):
        """
        Replaces all attributes of the student instance based on a dictionary
        """

    for key, value in json.items():
        setettr(self, key, value)
