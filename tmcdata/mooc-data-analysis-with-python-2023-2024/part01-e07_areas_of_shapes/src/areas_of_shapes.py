#!/usr/bin/env python3

import math


def main():
    """
    This function prompts the user to choose a shape and then
    calculates and prints the area of the chosen shape.

    The function keeps prompting the user for a shape until an
    empty string is entered.
    """

    while True:
        # Prompt the user for a shape
        shape = input("Choose a shape (triangle, rectangle, circle): ")

        # If the user enters an empty string, the loop is broken
        if shape == "":
            break

        # Convert the shape to lowercase for case-insensitive comparison
        shape = shape.lower()

        # Calculate and print the area of the chosen shape
        if shape == "triangle":
            # Prompt the user for the base and height of a triangle
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))

            # Calculate the area of a triangle
            area = 0.5 * base * height

            # Print the area
            print(f"The area is {area:.6f}")

        elif shape == "rectangle":
            # Prompt the user for the width and height of a rectangle
            width = float(input("Give base of the rectangle: "))
            height = float(input("Give height of the rectangle: "))

            # Calculate the area of a rectangle
            area = width * height

            # Print the area
            print(f"The area is {area:.6f}")

        elif shape == "circle":
            # Prompt the user for the radius of a circle
            radius = float(input("Give radius of the circle: "))

            # Calculate the area of a circle
            area = float(math.pi * radius**2)

            # Print the area
            print(f"The area is {area:.6f}")

        else:
            # If an unknown shape is entered, print an error message
            print("Unknown shape!")
 
     
 
if __name__ == "__main__":
     main()

 
