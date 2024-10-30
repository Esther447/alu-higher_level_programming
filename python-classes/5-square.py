#!/usr/bin/python3
"""Module that defines a Square class.

This module provides a Square class with methods to calculate
its area and print the square using a specified character.
"""

class Square:
    """Class that defines a square by its size.

    Attributes:
        size (int): The size of the square, must be a non-negative integer.

    Methods:
        area(): Returns the area of the square.
        my_print(): Prints the square using the '#' character.
    """

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character.

        If the size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
