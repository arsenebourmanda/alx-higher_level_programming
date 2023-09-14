#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixNew = matrix.copy()
    for elt in range(len(matrix)):
        matrixNew[elt] = list(map(lambda x: x**2, matrix[elt]))
    return (matrixNew)
