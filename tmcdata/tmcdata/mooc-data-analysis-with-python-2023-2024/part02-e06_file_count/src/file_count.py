#!/usr/bin/env python3

import sys

def file_count(filename):
    """
    Count the number of lines, words and characters in a file.

    This function reads a file and counts the number of lines, words
    and characters. The words are divided by splitting the text at
    whitespace. The numbers are returned as a tuple.

    :param filename: The name of the file to read.
    :return: A tuple containing the number of lines, words and characters.
    """
    with open(filename, "r") as file:
        content = file.read()
        chars =  len(content)
        words =  len(content.split())
        lines =  content.count('\n')  
        
    return lines, words, chars

def main():
     file_list = sys.argv[1:]
     
     for i in file_list:
         lines, words, chars = file_count(i)
         print(f"{lines}\t{words}\t{chars}\t{i}")

if __name__ == "__main__":
    main()
