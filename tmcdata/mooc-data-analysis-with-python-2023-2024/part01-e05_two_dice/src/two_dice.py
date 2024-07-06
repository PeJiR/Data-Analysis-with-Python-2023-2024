#!/usr/bin/env python3




def main():
    """
    This function is the main entry point of our program.
    It prints out all pairs of dice rolls that add up to 5.

    The main function iterates over the possible values of the first die.
    For each value, it iterates over the possible values of the second die.
    If the sum of the two dice is equal to 5, the pair of dice is printed.
    """

    # Iterate over the possible values of the first die
    for i in range(1, 7):  # Dice range from 1 to 6
        # Iterate over the possible values of the second die
        for j in range(1, 7):  # Dice range from 1 to 6
            # Check if the sum of the two dice is equal to 5
            if i + j == 5:  # If the sum of the dice is 5
                # If so, print the pair of dice
                print(f"({i},{j})")  # Print the dice values

if __name__ == "__main__":
    main()
