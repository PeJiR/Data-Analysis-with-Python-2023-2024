#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    """
    This function compares the second column of a matrix with the second-to-last
    column of the same matrix. It returns a new matrix containing the rows of the
    input matrix where the second column value is greater than the second-to-last
    column value.
    
    Parameters:
    a (numpy array): The input matrix.
    
    Returns:
    numpy array: The new matrix containing the rows where the second column value is
                greater than the second-to-last column value.
    """
    
    # Get the second column of the input matrix
    column_2 = a[:, 1]
    
    # Get the second-to-last column of the input matrix
    column_2nd_last = a[:, -2]
    
    # Compare the second column with the second-to-last column for each row
    condition = column_2 > column_2nd_last
    
    # Return the rows where the second column value is greater than the second-to-last column value
    return a[condition]
    
def main():
    a =np.array(
        [
            [8, 9, 3, 8, 8],
            [0, 5, 3, 9, 9],
            [5, 7, 6, 0, 4],
            [7, 8, 1, 6, 2],
            [2, 1, 3, 5, 8],                             
        ]          
    )
    print (column_comparison(a))
    

if __name__ == "__main__":
    main()
