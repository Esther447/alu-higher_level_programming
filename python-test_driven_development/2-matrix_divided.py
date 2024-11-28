#!/usr/bin/python3
"""
Module containing the matrix_divided function.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by div.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if rows are not of the same size, or if div is not a number.
        ZeroDivisionError: If div is zero.
        ValueError: If div is infinity or NaN.
    """
    # Check if arguments are provided
    if matrix is None or div is None:
        raise TypeError("matrix_divided() missing required arguments 'matrix' and/or 'div'")

    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows are of the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for special floating-point values (inf, nan)
    if div == float('inf') or div == float('-inf') or div != div:  # div != div checks for NaN
        raise ValueError("div must be a finite number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division
    return [[round(num / div, 2) for num in row] for row in matrix]
