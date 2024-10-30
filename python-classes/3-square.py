#!/usr/bin/python3
"""

This module defines a Square class with size validation and an area method."""


class Square:
    """

    A class that represents a square.
    """

    def __init__(self, size=0):
        """

        Initializes a new square with the given size.


        Args:
             Size (int): The size is not an integer.


        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        """

        calculates the area of the square.


        Returns:
            int: The area of the square.
        """

        return self.__size ** 2

