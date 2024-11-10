#!/usr/bin/python3
"""

This module contains a function
"""


def read_file(filename=""):
    """Reads a UTF-8 text and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
