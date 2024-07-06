#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load():
    """
    Load the iris dataset from a CSV file, drop the 'species' column, and return the values.
    
    Returns:
        numpy.ndarray: The iris dataset with the 'species' column removed.
    """
    
    # Import pandas library
    import pandas as pd
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv("src/iris.csv")
    
    # Drop the 'species' column from the DataFrame
    df = df.drop('species', axis=1)
    
    # Convert the DataFrame to a numpy array and return it
    return df.values

def lengths() -> float:
    """
    Calculate the Pearson correlation coefficient between the first and third columns of the iris dataset.

    Returns:
        float: The Pearson correlation coefficient between the first and third columns.
    """
    x: np.ndarray = load()
    
    return scipy.stats.pearsonr(x[:,0], x[:,2])[0]

def correlations() -> np.ndarray:
    """
    Calculate the correlation coefficients between all pairs of columns in the iris dataset.

    Returns:
        numpy.ndarray: A 2D array of correlation coefficients. The indices of the array correspond to the column pairs, and the values are the correlation coefficients between those pairs.
    """
    x: np.ndarray = load()
    
    return np.corrcoef((x[:,0], x[:,1], x[:,2], x[:,3]))


def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
