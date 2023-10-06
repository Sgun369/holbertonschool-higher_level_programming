#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared_row = []
        for value in row:
            if isinstance(value, int):
                squared_row.append(value ** 2)
            else:
                squared_row.append(value)
        result.append(squared_row)

    return result
