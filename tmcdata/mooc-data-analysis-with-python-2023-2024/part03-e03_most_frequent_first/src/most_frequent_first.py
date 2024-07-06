#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    """
    Returns an array of indexes in the input array `a` where the values in column `c` are sorted by frequency in descending order.

    Parameters:
        a (numpy.ndarray): The input array.
        c (int): The column index to sort by.

    Returns:
        numpy.ndarray: An array of indexes where the values in column `c` are sorted by frequency in descending order.
    """
    
    # Get the unique values and their counts in the specified column of the input array
    unique_values, unique_counts = np.unique(a[:, c], axis=0 ,return_counts=True)
    
    # Sort the unique values in descending order based on their counts
    count_sorted_identical = np.argsort(-unique_counts)
    
    # Get the unique values sorted by count
    val_sorted_by_count = unique_values[count_sorted_identical].reshape((1,-1))
    
    # Get the indexes of the values in the original array that match the sorted values
    # We use np.nditer to iterate over the sorted values and np.where to find the indexes of those values in the original array
    indexes_of_array = np.concatenate(
        [np.where((a[:,c]==x))[0] for x in np.nditer(val_sorted_by_count)]
    )
    
    # Return the indexes of the values in the original array sorted by count
    return a[indexes_of_array]

def main():
    a = np.array (        
        [
            [5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
            [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
            [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
            [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
            [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
            [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
            [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
            [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
            [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
            [5, 9, 3, 0, 5, 0, 1, 2, 4, 2],     
        ]
                       
    )    
    print(most_frequent_first(a, 0))
        

if __name__ == "__main__":
    main()
