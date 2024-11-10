#!/usr/bin/python3
class Student:
      """
    A class that defines a Student with attributes: first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with the provided values.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.
        Returns:
            dict: A dictionary containing the student's first name, last name, and age.
        """
        return self.__dict__

    def reload_from_json(self, json):
        """
        Updates the Student instance with values from a given dictionary.
        Args:
            json (dict): A dictionary containing new values for the student's attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
