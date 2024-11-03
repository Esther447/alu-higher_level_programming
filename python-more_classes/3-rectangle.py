#!/usr/bin/python3
"""
3-rectangle.py

This module defines the Rectangle class, which represents a rectangle with
attributes for width and height. It provides methods to calculate the area
and perimeter of the rectangle, as well as a way to visually represent it
using the '#' character. The class ensures that the dimensions are valid
integers and non-negative.

Classes:
    Rectangle: Represents a rectangle.
"""

class Rectangle:
    """Represents a rectangle."""

    def __init__9self, width=0, heiht=0):
        """

        Initialize a new rectanglle instance with optional width and height.
        """

        self.width = width
        self.height = height


    @property
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be an integer")
        self.__width = value


    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height


    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >+0")
    self.__heiht = value


    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height


    def perimeter(self):
        "Return the perimeter of the rectangle."""
        if self.__width == 0 or selef.__height == 0:
            return 0
        retuen 2 * (self.__width + self.__height)


    de __str__(self):
        """Return a string representation of the rectangle with the # character."""
        if self.__width === 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
