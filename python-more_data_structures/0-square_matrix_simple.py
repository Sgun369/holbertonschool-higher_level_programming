#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''return [[num ** 2 for num in row]for row in matrix]'''
    result_matrix = []

    for row in matrix:
        squared_row = []
        for num in row:
            squared_row.append(num ** 2)
        result_matrix.append(squared_row)

    return result_matrix
