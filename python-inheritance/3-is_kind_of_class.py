#!/usr/bin.python3
# 3-is_kind_of_class.py

"""
This module contains a function that checks if an object is an instance of a
specified class or if it is an instance of a class that inherited from the
specified class.

The module includes the following function:
- is_kind_of_class: Returns True if the object is an instance of the specified
  class or if the object is an instance of a subclass of the specified class;
  otherwise, it returns False.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class or
    if the object is an instance of a class that inherited from the specified class.
    Otherwise, it returns False.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is an instance of the specified class or
              an instance of a class that inherited from it; False otherwise.
    """
    return isinstance(obj, a_class)
