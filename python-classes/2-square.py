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

    @property
    def sizer(self):
        return self.__size

    def area(self):
        return self.__size ** 2

    @sizer.setter
    def sizer(self, size):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size


sq1 = Square(50)
