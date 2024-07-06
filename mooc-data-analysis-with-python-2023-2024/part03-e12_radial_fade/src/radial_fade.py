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
    X = np.full((height, weight), range(weight))
    
    # Calculate the radial distance from the center to each element
    return np.sqrt((Y - y) ** 2 + (X - x) ** 2)  # Use the Pythagorean theorem


def scale(a, tmin=0.0, tmax=1.0):
    """
    Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax].

    Args:
        a (ndarray): Input array.
        tmin (float, optional): Minimum value of the output range. Defaults to 0.0.
        tmax (float, optional): Maximum value of the output range. Defaults to 1.0.

    Returns:
        ndarray: Scaled array.
    """
    # Use numpy's interp function to scale the array.
    # The function takes three arguments:
    #   - x: The input array.
    #   - xp: Tuple of two arrays representing the input range.
    #   - fp: Tuple of two values representing the output range.
    return np.interp(a,(a.min(),a.max()),(tmin,tmax))

def radial_mask(a):
    """
    Calculate the radial mask of an array.

    The radial mask is defined as the scaled inverse of the radial distance from
    the center of the array to each element.

    Args:
        a (ndarray): Input array.

    Returns:
        ndarray: The radial mask of the array.
    """
    # Calculate the radial distance from the center of the array to each element
    radial_dist = radial_distance(a)
    
    # Calculate the inverse of the radial distance
    inverse_radial_dist = 1 / radial_dist
    
    # Scale the inverse radial distance to be in the range [0, 1]
    return scale(inverse_radial_dist)

def radial_fade(a):
    """
    Apply radial fade to array 'a'.

    The radial fade is defined as the element-wise multiplication of array 'a'
    with the radial mask of the array.

    Args:
        a (ndarray): Input array.

    Returns:
        ndarray: Radial faded array.
    """
    # Apply radial mask to the array. The mask is defined as the scaled inverse
    # of the radial distance from the center of the array to each element.
    # The mask is applied element-wise to the array.
    # The result is a new array where each element is multiplied with the
    # corresponding radial mask value.

    # The radial mask is calculated using the radial_mask function. The mask is
    # calculated for the array 'a' and the result is reshaped to match the
    # dimensions of the input array 'a'.
    # The reshape operation uses the newaxis argument to add a new axis to the
    # array. This is necessary because the multiplication operation between
    # two arrays requires the arrays to have the same number of dimensions.
    return  a * radial_mask(a)[:,:,np.newaxis]

def main():
    """
    Display an image with the radial mask and radial fade.

    This function reads an image file from the source directory and displays it
    using matplotlib. The image is displayed next to its radial mask and the
    result of applying the radial fade effect to the image.

    Parameters:
        None

    Returns:
        None
    """
    # Read the image file
    image = plt.imread("src/painting.png")

    # Create a figure with three subplots
    fig, ax = plt.subplots(3,1)

    # Display the original image
    ax[0].imshow(image)

    # Display the radial mask
    ax[1].imshow(radial_mask(image))

    # Display the radial fade
    ax[2].imshow(radial_fade(image))

    # Show the figure
    plt.show()

if __name__ == "__main__":
    main()
