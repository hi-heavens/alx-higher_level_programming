#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """This is to initialize a new square to an object.

        Args:
            size: The size of the square object
            position: The position of the square object
        """
        self.size = size
        self.position = position
   
    @property
    def size(self):
        """This is to retrieve the value of the size variable"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    @property
    def position(self):
        """This is to retrieve the value of the position variable"""
        return self.__position

    @position.setter
    def position(self, position):
        if len(position) != 2 or type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integer")
        if type(position[0]) != int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) != int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """This method returns the area of the size variable"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square using the # symbol"""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for num in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    def __str__(self):
        """This method returns the same behavior as my_print()"""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for num in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        return ""
