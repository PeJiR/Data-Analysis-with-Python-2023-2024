#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    """
    This function takes a string as parameter and returns a list of integers.
    The list of integers is composed of all integers that are enclosed in
    square brackets in the string.

    The function takes care of the following cases:
    - Input string is None
    - Input string is not a valid regular expression
    - Input string is not a valid input for the function
    - Input string contains non-integer values in the brackets

    :param s: the input string
    :type s: str
    :return: a list of integers
    :rtype: list[int]
    :raises ValueError: if the input string is None, does not match the regular expression, or contains non-integer values
    """
    if s is None:
        raise ValueError("Input string cannot be None")

    try:
        # Use regular expression to find all strings enclosed in square brackets
        # The regular expression matches strings of the form \[\s*[+-]?\d+)\s*\]
        # where [+-]?\d+) is a regular expression for an optional sign followed by one or more digits
        int_in_string = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)
    except re.error:
        # If the regular expression is invalid, raise a ValueError
        raise ValueError("Invalid regular expression in 'integers_in_brackets'") from None
    
    if int_in_string is None:
        # If the regular expression does not match the input string, raise a ValueError
        raise ValueError("Invalid input string in 'integers_in_brackets'")

    try:
        # Convert the list of strings to a list of integers
        return list(map(int, int_in_string))
    except TypeError:
        # If any of the values in the list are not integers, raise a ValueError
        raise ValueError("Invalid input string in 'integers_in_brackets'")
    
def main():
    """
    This function is the main entry point of the program. It does not take any parameters and does not return any values.
    """
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
