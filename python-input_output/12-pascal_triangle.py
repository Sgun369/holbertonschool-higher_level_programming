#!/usr/bin/python3
""""Pascal's Triangle module"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers
    representing the pascal's triangle of n"""
    if n <= 0:
        return []
    result = []

    for i in range(n):
        current_row = [1]

        for j in range(1, i):
            element = result[i - 1][j - 1] + result[i - 1][j]
            current_row.append(element)

        if i > 0:
            current_row.append(1)
        result.append(current_row)
    return result
