#!/usr/bin/env python3









def main():
    """
    This function is the main entry point of our program.
    It prints out all pairs of dice rolls that add up to 5.

    This function uses a list comprehension to generate all pairs of dice rolls
    that add up to 5. It iterates over the possible values of the first die,
    and for each value, it iterates over the possible values of the second die.
    If the sum of the two dice is equal to 5, the pair of dice is added to the
    list of dice pairs. Finally, the list of dice pairs is printed.
    """

    # Generate a list of all pairs of dice rolls that add up to 5
    dices = [(i, j) for i in range(1, 7)  # Iterate over the values of the first die
             for j in range(1, 7) if i + j == 5]  # Iterate over the values of the second die
                                                  # If the sum of the two dice is equal to 5

    # Print each pair of dice
    for dice in dices:
        print(f"({dice[0]}, {dice[1]})")  # Print each pair of dice

if __name__ == "__main__":
    main()
