#!/usr/bin/python3
"""
Module containing the matrix_divided function.
"""


def matrix_divided(matrix=None, div=None):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: list of lists of integers/floats.
        div: number (integer/float).

    Returns:
        A new matrix with each element divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix or div are not valid types.
        ZeroDivisionError: If div is 0.
    """
    # Check if arguments are missing
    if matrix is None:
        raise TypeError("matrix is missing")
    if div is None:
        raise TypeError("div is missing")

    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix with rounded values
    return [[round(x / div, 2) for x in row] for row in matrix]
