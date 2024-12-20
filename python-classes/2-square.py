#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute
and size validation.
"""


class Square:
    """
    A class that represents a square.
    """
    def __init__(self, size=0):
        """
        Initializes a new square with the given size.

        Args:
            size (int): The size of the square, defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
