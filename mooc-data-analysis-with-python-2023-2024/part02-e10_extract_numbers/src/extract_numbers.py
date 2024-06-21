#!/usr/bin/env python3

def extract_numbers(s):
    """
    Extracts all integers and floats from a string and returns them as a list.
    """
    numbers = []
    words = s.split()

    for word in words:
        try:
            numbers.append(int(word))
        except ValueError:
            try:
                numbers.append(float(word))
            except ValueError:
                pass

    return numbers

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
