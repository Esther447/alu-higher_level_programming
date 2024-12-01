#!/usr/bin/python3
"""
Main entry point for the Python Almost a Circle project.
This file demonstrates how to use the Base, Rectangle, and Square classes.
"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

def main():
    """Test the functionality of the Base, Rectangle, and Square classes."""
    
    # Create instances of Base, Rectangle, and Square
    base_instance = Base()
    print("Base instance ID: {}".format(base_instance.id))  # Using .format()

    rectangle = Rectangle(10, 5)
    print("Rectangle: width={}, height={}, id={}".format(rectangle.width, rectangle.height, rectangle.id))  # Using .format()

    square = Square(4)
    print("Square: size={}, id={}".format(square.size, square.id))  # Using .format()

if __name__ == "__main__":
    main()
