#!/usr/bin/python3

# 3-is_kind_of_class.py
"""
Module to check if an object is an instance of a specified class or
if the object is an instance of a subclass of the specified class.

This module contains one function:

    is_kind_of_class(obj, a_class): Returns True if the object is an instance
                                    of a_class or an instance of a subclass
                                    of a_class, otherwise False.


def is_kind_of_class(obj, a_class):
"""
    Checks if an object is an instance of a specified class or an instance
    of a class that inherited from the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is an instance of the specified class or 
              an instance of a class that inherited from it; False otherwise.
    """

    return isinstance(obj, a_class)
