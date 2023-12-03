#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        if n != '[' or n != ']':
            print(n)
