#!/usr/bin/python3
"""
This module provides a function to convert a JSON string into a Python data structure.

The 'from_json_string' function takes a JSON string as input and returns the
corresponding Python object.
"""

import json

def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.

    Args:
        my_str (str): A JSON-formatted string.

    Returns:
        object: A Python object represented by the JSON string, such as a
                list, dictionary, integer, or string.

    Example:
        >>> from_json_string('[1, 2, 3]')
        [1, 2, 3]
    """ 
    return json.loads(my_str)
