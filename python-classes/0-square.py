#!/usr/bin/python3
class Square:
    """
    A class made for calculating the size of square
    """
    def Size(self, size):
        """
        Function to take size and made it private
        Args:
            size(int): size must be integer
        Returns:
            size in a private attribute
        """
        self.__size = size


sq1 = Square()
sq1.size = 55
