#!/usr/bin/python3
"""Create a Class Square with size, method of area and getters & setters"""


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

    @property
    def size(self):
        """Getter of the private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the size private attribute"""
        if ((type(value) is int) or (type(value) is float)):
            if (value < 0):
                raise (ValueError("size must be >= 0"))
        else:
            raise (TypeError("size must be a number"))
        self.__size = value

    def __lt__(self, other):
        """Compare operator <"""
        return (self.area() < other.area())

    def __le__(self, other):
        """Compare operator <="""
        return (self.area() <= other.area())

    def __gt__(self, other):
        """Compare operator >"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Compare operator >="""
        return (self.area() >= other.area())

    def __eq__(self, other):
        """Compare operator =="""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Compare operator !="""
        return (self.area() != other.area())

    def area(self):
        """Method to get the area of the Square"""
        return (self.__size ** 2)
