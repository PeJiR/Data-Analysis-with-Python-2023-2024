#!/usr/bin/env python3



def find_matching(L, pattern):
    """
    Find the indices of elements in a list that contain a given pattern.

    Args:
    L (list): The list to search in.
    pattern (str): The pattern to search for.

    Returns:
    list: A list of indices where the pattern is found.
    """

    # Initialize an empty list to hold the indices.
    indices = []

    # Iterate over the list and find the indices where the pattern is found.
    for i, x in enumerate(L):
        if pattern in x:
            indices.append(i)

    # Return the list of indices.
    return indices



def main():
    pass

if __name__ == "__main__":
    main()
