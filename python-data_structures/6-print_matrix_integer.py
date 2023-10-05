#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
        return
    for row in matrix:
        row_str = " ".join(map(str, row))
        print("{}".format(row_str))
