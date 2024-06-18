#!/usr/bin/env python3
import re

def word_frequencies(filename):
    """
    Calculate the frequency of each word in a file.

    Parameters:
        filename (str): The name of the file to read.

    Returns:
        dict: A dictionary where the keys are the words in the file and the values are the frequencies of each word.
    """
    results = {}
    with open(filename) as file:

        for line in file:
            
                # Match everything expect whitespaces
                regex = re.findall(r"(\S*)", line)
                
                # strip according to the assigment
                regex = [match.strip("""!"#$%&'()*,-./:;?@[]_""") for match in regex]

                # fill in the dictionary with counts
                for regex_match in regex:
                    if regex_match in results:
                        results[regex_match] += 1
                    else:
                        results[regex_match] = 1

    return results


def main():
    """
    Executes the main function of the program.

    This function calls the `word_frequencies` function with the argument "alice.txt" to calculate the frequency of each word in the file.

    Parameters:
        None

    Returns:
        None
    """
    word_frequencies("alice.txt")


if __name__ == "__main__":
    main()
