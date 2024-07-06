#!/usr/bin/env python3

def sum_equation(L):
    """
    Generate an equation string from a list of numbers.

    If the list is empty, the function returns "0 = 0".

    Parameters
    ----------
    L : list
        List of numbers.

    Returns
    -------
    equation : str
        Equation string.
    """
    if not L:
        return "0 = 0"
    else:
        total = sum(L)
        equation = " + ".join(str(x)for x in L) + " = " + str(total)
        return equation

def main():
    print(sum_equation([1, 5, 7]))  # Output: "1 + 5 + 7 = 13"
    print(sum_equation([]))  # Output: "0 = 0"

if __name__ == "__main__": 
    main()
