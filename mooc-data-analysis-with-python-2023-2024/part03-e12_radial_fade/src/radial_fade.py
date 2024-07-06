#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    """
    Returns the center coordinates of the array 'a'.
    
    Args:
        a (ndarray): Input array.
        
    Returns:
        tuple: Center coordinates of the array.
    """
    # Calculate the center coordinates of the array.
    # The order of coordinates is (center_y, center_x).
    dimensions = a.shape
    center_y = (dimensions[0] - 1) / 2
    center_x = (dimensions[1] - 1) / 2
    return (center_y, center_x)
    

def radial_distance(a):
    """
    Calculate the radial distance from the center of an array to each element.
    
    Args:
        a (ndarray): Input array.
    
    Returns:
        ndarray: The radial distance from the center of the array to each element.
    """
    # Get the dimensions of the input array
    height, weight = a.shape[0], a.shape[1]
    
    # Calculate the center coordinates of the array
    y, x = center(a)
    
    # Create arrays of y and x coordinates
    Y = np.full((weight, height), range(height)).T  # Transpose to match element order
    X = np.full((weight, height), range(weight))
    
    # Calculate the radial distance from the center to each element
    return np.sqrt((Y - y) ** 2 + (X - x) ** 2)  # Use the Pythagorean theorem


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.array([[]])

def radial_mask(a):
    return np.array([[]])

def radial_fade(a):
    return np.array([[]])

def main():
    pass

if __name__ == "__main__":
    main()
