#!/usr/bin/python3
"""
This module defines a Rectangle class for representing rectangles.

The Rectangle class includes private instance attributes for width and height,
public class attributes to keep track of instances and customize print symbols,
and methods for calculating area, perimeter, and comparing rectangles.

The class also handles instance deletion with a custom message and supports
printing and recreating instances using str() and repr(), and includes a class
method to create square rectangles.
"""


class Rectangle:
    """Defines a rectangle with w & h attributes, along with various methods.

    Attributes:
        number_of_instances (int): Tracks the number of Rectangle instances.
        print_symbol (str): Symbol used for string represent rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute with validation.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute with validation.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Creates a string representation of the rectangle using the print_symbol.

        Returns:
            str: String represent of the rectangle, empty string if w,h is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
 return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """Returns a string representation of the rectangle for recreating the instance.

        Returns:
            str: The representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Called when a Rectangle instance is deleted. Decrements the instance counter and prints a message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the one with the greater area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the greater or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width and height equal to size.

        Args:
            size (int): The size of the rectangle's sides.

        Returns:
        Rectangle: New Rectangle instance where w & h are equal to size.
        """
        return cls(size, size)
