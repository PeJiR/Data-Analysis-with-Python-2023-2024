#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    This function plots two graphs on the same plot using matplotlib.pyplot.

    The two graphs are defined by two sets of x and y coordinates.
    """
    # Define the x and y coordinates of the first graph
    x1 = np.array([2, 4, 6, 7])
    y1 = np.array([4, 3, 5, 1])

    # Define the x and y coordinates of the second graph
    x2 = np.array([1, 2, 3, 4])
    y2 = np.array([4, 2, 3, 1])

    # Plot the first graph
    plt.plot(x1, y1)

    # Plot the second graph
    plt.plot(x2, y2)

    # Set the title of the plot
    plt.title("Multiple graphs")

    # Set the x-axis label
    plt.xlabel("x")

    # Set the y-axis label
    plt.ylabel("y")

    # Show the plot
    plt.show()
    
    
if __name__ == "__main__":
    main()