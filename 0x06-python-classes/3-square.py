#!/usr/bin/python3
"""defines a square """


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """ Initializes the size of the square"""
        if (type(size) is int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """ Calculating the area of the square """
        return self.__size ** 2
