#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            print("{:d}".format(matrix[col][row]), end="")
            if row != (len(matrix[col]) - 1):
                print(" ", end="")
        print("")
