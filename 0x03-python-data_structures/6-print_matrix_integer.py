#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lie in matrix:
        for colon in lie:
            print("{:d}".format(colon), end=" " if colon != lie[-1] else "")
        print()
