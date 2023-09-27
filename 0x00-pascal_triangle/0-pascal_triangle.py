#!/usr/bin/python3
"""Function to Implement Pascal's Triangle"""


def pascal_triangle(n):
    """Prints a pascal triangle"""
    if n <= 0:
        return []

    # Creates an empty triangle
    
    triangle = [[1]]

    # Fills the triangle with rows
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
