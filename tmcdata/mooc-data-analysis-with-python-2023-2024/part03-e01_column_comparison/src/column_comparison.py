#!/usr/bin/env python3

import numpy as np



def column_comparison(a):
    """
    This function compares the second column of a matrix with the second-to-last
    column of the same matrix. It returns a new matrix containing the rows of the
    input matrix where the second column value is greater than the second-to-last
    column value.

    Parameters
    ----------
    a : numpy array
        The input matrix.

    Returns
    -------
    numpy array
        The new matrix containing the rows where the second column value is
        greater than the second-to-last column value.
    """

    # Get the second column of the input matrix
    column_2 = a[:, 1]  # Second column of the matrix

    # Get the second-to-last column of the input matrix
    column_2nd_last = a[:, -2]  # Second-to-last column of the matrix

    # Compare the second column with the second-to-last column for each row
    # Create a boolean array indicating where the condition is true
    condition = column_2 > column_2nd_last

    # Return the rows where the second column value is greater than the second-to-last column value
    return a[condition]
    
def main():
    """
    Main function to test the column_comparison function.
    
    This function creates a sample matrix 'a' and prints the result of the
    column_comparison function. The column_comparison function compares the
    second column of 'a' with the second-to-last column of 'a'. It returns a
    new matrix containing the rows where the second column value is greater
    than the second-to-last column value.
    
    The rows of 'a' represent different data points and the columns represent
    different attributes of the data points. The values in the columns represent
    different features of the data points.
    
    The column_comparison function is called with the sample matrix 'a'. The
    result of the function is stored in the variable 'result'. Finally, the
    result is printed.
    """
    
    # Create a sample matrix 'a'
    # The rows represent different data points
    # The columns represent different attributes of the data points
    # The values in the columns represent different features of the data points
    a = np.array(
        [
            [8, 9, 3, 8, 8],  # First data point
            [0, 5, 3, 9, 9],  # Second data point
            [5, 7, 6, 0, 4],  # Third data point
            [7, 8, 1, 6, 2],  # Fourth data point
            [2, 1, 3, 5, 8],  # Fifth data point
        ]
    )
    
    # Call the column_comparison function with the sample matrix 'a'
    # The function returns a new matrix containing the rows where the second
    # column value is greater than the second-to-last column value
    result = column_comparison(a)
    
    # Print the result of the column_comparison function
    # The result is a new matrix containing the rows where the second column value
    # is greater than the second-to-last column value
    print(result)
    

if __name__ == "__main__":
    main()
