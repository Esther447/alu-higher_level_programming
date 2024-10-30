#!/usr/bin/python3
"""

This module defines a square class with a private instance attribute.
"""


class Square:
    """

    A class that represents a square.
    """

    def __init__(self, size):
        """

        Initializes a new square with the given size.

        Args:
            Size (int): The size of the square.
        """

        self.__size = size