#!/usr/bin/env python3


def detect_ranges(L):
    """
    Detect ranges of consecutive numbers in a given list.

    Args:
    L (list): The list of numbers to detect ranges from.

    Returns:
    list: A list of tuples, where each tuple represents a range of consecutive numbers.
    """
    # Sort the input list
    L_sorted = sorted(L)

    # Initialize an empty list to hold the ranges
    result = []

    # Initialize an index for the sorted list
    i = 0

    # Loop through the sorted list
    while L_sorted:
        # If only one element is left, append it to result and remove it from L_sorted
        if len(L_sorted) == 1:
            result.append(L_sorted[0])
            L_sorted.pop(0)
        # If the next element is one more than the current element, extend the current range
        elif L_sorted[i + 1] == L_sorted[i] + 1:
            i += 1
            # If the next element is the last element, form a range and reset L_sorted
            if i == len(L_sorted) - 1:
                temp = (L_sorted[0], L_sorted[i] + 1)
                L_sorted = []
                result.append(temp)
        # If not, form a range, reset L_sorted, and reset the index
        else:
            if i == 0:
                result.append(L_sorted[0])
                L_sorted.pop(0)
            else:
                temp = (L_sorted[0], L_sorted[i] + 1)
                del L_sorted[:i + 1]
                result.append(temp)
                i = 0
    
    # Return the list of ranges
    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
