#!/usr/bin/python3
"""We are going to define the class here"""


class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0):
        """Initialization of the size field"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """return the current square area"""
        return self.__size ** 2
