#!/usr/bin/python3
"""
This module provides a function to convert a JSON string into a Python data structure.

The 'from_json_string' function takes a JSON string as input and returns the
corresponding Python object.
"""

import json

def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.""" 
    return json.loads(my_str)
