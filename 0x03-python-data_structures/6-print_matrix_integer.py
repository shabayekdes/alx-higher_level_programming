#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            end = " "
            if col == row[-1]:
                end = ""
            print("{:d}".format(col), end=end)
        print()
