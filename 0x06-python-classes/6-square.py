#!/usr/bin/python3
"""defines a square """


class Square:
    """A class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object
        """
        self.size = size
        self.position = position

    def area(self):
        """ Calculating the area of the square """
        return self.__size ** 2
    
    def my_print(self):
        """Method to print a Square with spaces"""
        if (self.__size == 0):
            print()
        else:
            for blank in range(self.position[1]):
                print()
            for rows in range(self.__size):
                print(" " * self.position[0], end='')
                print("#" * self.__size)
                
    @property
    def size(self):
        """ gets the size of the square"""
        return self.__size
    
    @property
    def position(self):
        """ Method that returns the position value
        """
        return self.__position

    @size.setter
    def size(self, value):
        """ Method that sets the new size of the square"""
        if (type(value) is int):
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter of position"""
        if (len(value) != 2) or (type(value) is not tuple) \
                or (type(value[0]) is not int) \
                or (type(value[1]) is not int) \
                or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
