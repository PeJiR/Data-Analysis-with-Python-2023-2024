#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    """Calculate the solutions to a quadratic equation.
    
    Args:
        a (float): Coefficient of x^2
        b (float): Coefficient of x^1
        c (float): Constant term
    
    Returns:
        tuple: A tuple with the two solutions (x1, x2) or a string if the
        discriminant is less than 0.
    """
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    
    # check if the discriminant is less than 0
    if d < 0:
        return "Discriminant can't be less than 0"
        
    # calculate the solutions
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    
    return (x1, x2)
         


def main():
    print(solve_quadratic(1,2,3))

if __name__ == "__main__":
    main()
