#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for colonne in ligne:
            break1 = "{:d}".format(colonne)
            break2 = end=" " if colonne != ligne[-1] else ""
            print(break1, break2)
        print()
