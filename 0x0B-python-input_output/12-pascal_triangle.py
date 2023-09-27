#!/usr/bin/python3
"""module for pascal_triangle"""


def pascal_triangle(n):
    """creates pascals triangle"""
    if n <= 0:
        return []
    else:
        triangle = [[1]]
        i = 1
        while i < n:
            row = [1]
            j = 1
            while j < i:
                num = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(num)
                j = j + 1
            row.append(1)
            triangle.append(row)
            i = i + 1

        return triangle
