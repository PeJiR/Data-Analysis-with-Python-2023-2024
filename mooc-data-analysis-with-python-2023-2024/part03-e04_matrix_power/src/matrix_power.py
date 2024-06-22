#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a: np.ndarray, n: int) -> np.ndarray:
    """
    Calculate the matrix power of a given matrix.

    Args:
        a (np.ndarray): The matrix to calculate the power of.
        n (int): The exponent.

    Returns:
        np.ndarray: The matrix power.

    Raises:
        ValueError: If n is not an integer.

    This function calculates the matrix power of a given matrix a raised to the power of n.
    If n is 0, it returns the identity matrix of the same size as a.
    If n is positive, it multiplies a by itself n times.
    If n is negative, it calculates the inverse of a and multiplies it by itself |n| times.
    """
    if not isinstance(n, int):
        raise ValueError("The exponent must be an integer!")
    if n == 0:
        # Return the identity matrix of the same size as a
        return np.eye(a.shape[0], dtype=a.dtype)
    elif n > 0:
        # Multiply a by itself n times
        return reduce(np.matmul, [a for _ in range(n)])
    else:
        # Calculate the inverse of a and multiply it by itself |n| times
        inv_a = np.linalg.inv(a)
        return reduce(np.matmul, [inv_a for _ in range(-n)])

def main():
    a = np.array([[0, 1], [-1, 0]])
    print(matrix_power(a, -3))

if __name__ == "__main__":
    main()
