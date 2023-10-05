#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
    lena = len(matrix)
    for a in range(lena):
        lenb = len(matrix[a])
        for b in range(lenb):
            if b == lenb - 1:
                print("{:d}".format(matrix[a][b]))
            else:
                print("{:d}".format(matrix[a][b]), end=" ")
