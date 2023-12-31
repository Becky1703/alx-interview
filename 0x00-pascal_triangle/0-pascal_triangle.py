#!/usr/bin/python3
"""Function to Implement Pascal's Triangle"""


def pascal_triangle(n):
    """Prints a pascal triangle"""
    if n <= 0:
        return []

    # Creates an empty triangle

    triangle = []

    # Fills the triangle with rows
    for row_num in range(n):
        row = [None for _ in range(row_num + 1)]
        row[0], row[-1] = 1, 1

        for j in range(1, len(row) - 1):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)

    return triangle
