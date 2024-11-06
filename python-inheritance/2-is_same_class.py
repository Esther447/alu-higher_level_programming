#!/usr/bin/python3
"""
This module defines a function to check if an object is exactly an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly instance of a_class, otherwise False."""
    return type(obj) is a_class
