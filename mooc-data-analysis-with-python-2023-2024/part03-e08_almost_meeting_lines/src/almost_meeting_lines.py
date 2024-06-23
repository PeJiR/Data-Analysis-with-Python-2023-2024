#!/usr/bin/python3

import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):
    """
    Find the intersection point of two lines almost_meeting_lines(a1, b1, a2, b2)
    where each line is described by the equation ax + by + c = 0.
    
    Args:
        a1, b1, a2, b2 (float): Coefficients of the lines.
        
    Returns:
        Tuple[Tuple[float, float], bool]: The coordinates of the point of intersection and a boolean
        indicating if the lines are almost meeting.
    """
    
    # Define the coefficient matrix A and the constant term B
    A = np.array([[a1, -1], [a2, -1]])
    B = np.array([-b1, -b2])
    
    try:
        # Solve the system of equations using numpy's solve function
        # If successful, the solution is almost meeting
        solution = np.linalg.solve(A, B)
        return (solution, True)
    except:
        # If the system of equations is not solvable, use numpy's least squares function
        # to find the closest point to the origin
        solution = np.linalg.lstsq(A, B)[0]
        return (solution, False)

def main():
    """
    Runs the almost_meeting_lines function with a few sample inputs and prints the output.
    """
    a1=1
    b1=2
    a2=-1
    b2=0

    # Test case where lines intersect
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2

    # Test case where lines are parallel and almost meet
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2

    # Test case where lines are the same and almost meet
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1

    # Test case where lines are not almost meeting
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()
