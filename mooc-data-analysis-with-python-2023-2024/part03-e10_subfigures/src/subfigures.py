#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    """
    Plots data on a subplot of two subplots.
    
    Parameters
    ----------
    a : numpy.ndarray
        Data to be plotted. Each row represents a data point. The first two
        columns represent the x and y values, respectively. The third column
        represents the color of each point, and the fourth column represents
        the size of each point.
    """
    # Create a figure with two subplots
    figure_plot, axis_plot = plt.subplots(1,2)
    
    # Plot the first two columns of data on the first subplot
    axis_plot[0].plot(a[:,0], a[:,1])
    # Plot the first two columns of data on the second subplot, with each point
    # having a color and size specified by the third and fourth columns of data,
    # respectively.
    axis_plot[1].scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    
    # Show the plot
    plt.show()
    
    
def main():
    """
    Generate the data and plot it using subfigures function.

    This function creates a numpy array 'a' with four columns. The first two
    columns represent the x and y values, respectively. The third column
    represents the color of each point, and the fourth column represents
    the size of each point.

    The subfigures function is then called with 'a' as the argument.
    """
    # Create a numpy array 'a' with four columns
    # The first two columns represent the x and y values, respectively.
    # The third column represents the color of each point, and the fourth column
    # represents the size of each point.
    a = np.column_stack([[1, 2, 3], [2, 4, 6], [0.24, 2.99, -1.49], [25, 50, 10]])

    # Call the subfigures function with 'a' as the argument
    subfigures(a)
    

if __name__ == "__main__":
    main()
