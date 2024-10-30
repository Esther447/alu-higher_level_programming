#!/usr/bin/python3
class Square:
    """Class that defines a square by its size.


    Attributes:
        size (int): The size of the square, must be a non-negative integer.

    Methods:
        area(): Returns the area of the square.
        my_print(): Prints the square using the '#' character.
    """


    def __init__(self, size=0):
        self.size = size


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
