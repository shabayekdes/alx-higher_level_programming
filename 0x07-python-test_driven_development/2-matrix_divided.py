#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides all element of a matrix
    """
    my_list = []
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(message)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(message)
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        temp_list = []
        for number in row:
            if type(number) is not int and type(number) is not float:
                raise TypeError(message)
            temp_list.append((round((number / div), 2)))
        my_list.append(temp_list)
    return my_list


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
