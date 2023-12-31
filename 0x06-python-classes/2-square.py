#!/usr/bin/python3
"""defines a square """


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """initializes the size"""
        if (type(size) is int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = size
