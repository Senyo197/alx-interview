#!/usr/bin/python3
"""Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise in-place.
    
    :param matrix: List[List[int]] - The n x n 2D matrix to be rotated.
    :return: None - The matrix is rotated in place, no return value.
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
