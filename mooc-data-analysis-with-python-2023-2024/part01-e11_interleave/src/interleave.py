#!/usr/bin/env python3

def interleave(*lists):
    """
    Interleave elements from multiple lists.

    Args:
        *lists (iterable): One or more iterables.

    Returns:
        list: A list with elements interleaved from the input lists.
    """
    # Initialize an empty list to store the interleaved elements
    interleave_list = []

    # Use zip() function to interleave elements from multiple lists
    for x in zip(*lists):
        # Extend the interleave_list with the interleaved elements
        interleave_list.extend(x)

    # Return the interleaved list
    return interleave_list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
