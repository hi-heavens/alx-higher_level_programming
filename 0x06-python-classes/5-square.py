#!/usr/bin/python3
"""We are going to define the class here"""


class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0):
        """Initialization of the size field"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the current square area"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for num in range(self.__size):
                for number in range(self.__size):
                    print('#', end="")
                print()
