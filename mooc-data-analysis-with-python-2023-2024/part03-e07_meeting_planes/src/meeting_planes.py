#!/usr/bin/python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    """
    Solves the system of equations given by the planes defined by the lines
    ax + by + cz + d = 0.
    
    Args:
        a1, b1, c1, a2, b2, c2, a3, b3, c3 (float): Coefficients of the planes.
    
    Returns:
        Tuple[float, float, float]: The coordinates of the point where the
        planes meet.
    """
    # Define the coefficient matrix A and the constant term B
    A = np.array([
        [a1, b1, -1],
        [a2, b2, -1],
        [a3, b3,-1]
    ])
    
    B = np.array([-c1,-c2,-c3])
    
    # Solve the system of equations using numpy's solve function
    solution = np.linalg.solve(A, B)
    
    # Extract the coordinates of the point where the planes meet
    y, x, z = np.round(solution,3)
    
    return x, y, z

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
