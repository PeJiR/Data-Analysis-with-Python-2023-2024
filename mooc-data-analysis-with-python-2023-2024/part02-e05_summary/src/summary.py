#!/usr/bin/env python3

import sys
import re
import math


def summary(filename: str) -> tuple:
    """
    Summarize the numeric values in a file.

    This function reads a file and extracts all the numeric values.
    It then calculates the total, average and standard deviation
    of the numeric values.

    :param filename: The name of the file to read.
    :return: A tuple containing the total, average and standard deviation.
    """
    with open(filename, "r") as file:
        # Find the numeric values into a file
        # The regular expression finds all occurrences of
        # numbers in the file. The numbers can be signed and
        # can have decimal points.
        numbers_in_list = [
            float(num) for num in re.findall(r"([+|-]*\d+(?:\.\d*)?)", file.read())
        ]

        # The number of numeric values
        count = len(numbers_in_list)

        # The total of the numeric values
        total = sum(numbers_in_list)

        # The average of the numeric values
        avg = total / count

        # Calculate the sum of (x - avg)^2
        # This is a formula for calculating the variance
        # of a set of numbers.
        mean_squared_diff = sum((num - avg) ** 2 for num in numbers_in_list)

        # The standard deviation of the numeric values
        # is the square root of the variance divided
        # by the degrees of freedom. The degrees of
        # freedom is the number of data points minus
        # one.
        std = math.sqrt(mean_squared_diff / (count - 1))

    return total, avg, std


def main():
    for filename in sys.argv[1:]:
        total, avg, std = summary(filename)
        print(f"File: {filename} Sum: {total:.6f} Average: {avg:.6f} Stddev: {std:.6f}", end="\n")


if __name__ == "__main__":
    main()
