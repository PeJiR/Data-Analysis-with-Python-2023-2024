#!/usr/bin/env python3

def distinct_characters(L):
    """
    Given a list of strings, this function returns a dictionary where each string is a key and the value
    associated with that key is the number of distinct characters in that string.

    Parameters:
    L (list): A list of strings.

    Returns:
    dict: A dictionary where each key is a string and the value is the number of distinct characters in that string.
    """

    # Initialize an empty dictionary to store the results.
    result = {}

    # Iterate over each string in the input list.
    for string in L:

        # Create a set of distinct characters in the current string.
        distinct_chars = set(string)

        # Associate the number of distinct characters in the current string with the current string as the value in the result dictionary.
        result[string] = len(distinct_chars)

    # Return the result dictionary.
    return result

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
