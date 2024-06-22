#!/usr/bin/python3

import numpy as np



def meeting_lines(a1, b1, a2, b2):
    """
    Given two lines in slope-intercept form (y = a*x + b),
    calculate the point where they meet.

    Args:
        a1 (float): The slope of the first line
        b1 (float): The y-intercept of the first line
        a2 (float): The slope of the second line
        b2 (float): The y-intercept of the second line

    Returns:
        tuple: The x and y coordinates of the point where the lines meet
    """

    # Create a 2x2 matrix with the coefficients of the two lines.
    # The first column contains the slopes of the lines, and the
    # second column contains -1 (since the y-intercept is the same
    # for both lines).
    matrix = np.array([[a1, -1], [a2, -1]])

    # Create a 1D array with the negative of the y-intercepts of the two lines.
    # The y-intercept of the first line is b1, and the y-intercept of the second
    # line is b2. We negate these values to get the array of constants.
    constants = np.array([-b1, -b2])

    # Solve the system of linear equations using numpy's linalg.solve function.
    # The matrix and constants arrays are used to represent the equations:
    # a1*x + y = b1
    # a2*x + y = b2
    # The solution to this system of equations is the point where the lines meet.
    point = np.linalg.solve(matrix, constants)

    # Return the x and y coordinates as a tuple.
    # The first element of the point array is the x-coordinate,
    # and the second element is the y-coordinate.
    return point[0], point[1]

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
