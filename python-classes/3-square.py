#!/usr/bin/python3
"""
This module created for defining squares
based on private size attribute
"""


class Square:
    """
    This class used for defining size
    of square
    """

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size


sq1 = Square(50)
