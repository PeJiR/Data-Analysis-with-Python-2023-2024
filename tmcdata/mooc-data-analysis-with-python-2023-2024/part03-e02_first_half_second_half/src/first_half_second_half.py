#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a: np.ndarray) -> np.ndarray:
    """
    Given a 2D numpy array `a`, this function returns a subset of `a` where each row is selected if the sum of the elements
    in the first half of the row is greater than the sum of the elements in the second half of the row.
    
    Parameters:
    -----------
    a : numpy.ndarray
        A 2D numpy array.
        
    Returns:
    --------
    numpy.ndarray
        A subset of `a` where each row is selected if the sum of the elements in the first half of the row is greater than
        the sum of the elements in the second half of the row.
    """
    # Determine the middle index
    middle_index = int(a.shape[1] / 2)
    
    # Determine if the first half is larger than the second half
    # Calculate the sums of the elements in the first and second halves of each row
    first_half_sums: np.ndarray = np.sum(a[:, :middle_index], 1)  # First half sums
    second_half_sums: np.ndarray = np.sum(a[:, middle_index:], 1)  # Second half sums
    
    # Compare the sums of the first and second halves to determine if the first half is larger
    greater_than: np.ndarray = first_half_sums > second_half_sums
    
    # Return a subset of a containing only the rows where the first half is larger
    return a[greater_than]


def main():
    a = np.array([[1, 3, 4, 2], [2, 2, 1, 2]])
    print(first_half_second_half(a))


if __name__ == "__main__":
    main()
