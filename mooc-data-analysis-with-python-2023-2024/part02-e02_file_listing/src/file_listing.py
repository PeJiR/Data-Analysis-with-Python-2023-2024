#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    """
    Reads a file and extracts file information from each line.

    Args:
        filename (str, optional): The path to the file to be read. Defaults to "src/listing.txt".

    Returns:
        list: A list of tuples, where each tuple contains the following information in order:
            - filesize (int): The size of the file.
            - month (str): The month of the file's last modification.
            - day (int): The day of the file's last modification.
            - hour (int): The hour of the file's last modification.
            - minute (int): The minute of the file's last modification.
            - filename (str): The name of the file.
    """
    # Create list to store regex matches
    results= []
    
    # Read the file and find the files
    with open(filename,"r") as file:
        for line in file:
             # Get the filesize, date and filename from a single line(skip empty lines )
             regex = re.findall(
                 r"\S+\s\d\s\w+\s\S+\s+(\d+)\s([A-Za-z]{3})\s+(\d{1,})\s(\d{2}):(\d{2})\s(.+)",
                line,
             )
             
             # Create a tuple and append the results
             regex = (
                 int(regex[0][0]),
                 regex[0][1],
                 int(regex[0][2]),
                 int(regex[0][3]),
                 int(regex[0][4]),
                 regex[0][5],
             )
             results.append(regex)
                    
    return results

def main():
    """
    Executes the main function.

    This function calls the `file_listing` function and prints the result.

    Parameters:
        None

    Returns:
        None
    """
    print(file_listing())

if __name__ == "__main__":
    main()
