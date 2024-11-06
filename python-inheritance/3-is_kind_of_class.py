#!/usr/bin/python3
"""
Module to check if an object is an instance of a specified class or
if the object is an instance of a subclass of the specified class.

This module contains one function:

    is_kind_of_class(obj, a_class): Returns True if the object is an instance
                                    of a_class or an instance of a subclass
                                    of a_class, otherwise False.
"""


# 3-is_kind_of_class.py

def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
