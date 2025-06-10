#!/usr/bin/python3
"""We are going to define the class here"""


class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the size field"""
        self.size = size
        self.position = position

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
            print('\n' * self.__position[1], end='')
            for num in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
