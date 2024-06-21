#!/usr/bin/env python3

 
from src import triangle
 

def main():
    """
    This is the main function of the usemodule module.

    It calls the hypotenuse and area functions from the triangle module
    and prints their results.
    """

    # Call the functions from here
    print(triangle.hypotenuse(10, 20))  # Print the length of the hypotenuse of a right-angled triangle
    print(triangle.area(10, 20))  # Print the area of a right-angled triangle

if __name__ == "__main__":
    main()