#!/usr/bin/env python3


def acronyms(s):
    """
    Extracts acronyms from a given string.
    
    Args:
        s (str): The input string.
    
    Returns:
        list: A list of acronyms.
    """
    
    # Split the string into words and remove leading and trailing parentheses, commas, and dots
    words = [word.strip("(,), .") for word in s.split()]
    
    # Filter the words to keep only those that are in uppercase and have a length greater than or equal to 2
    acronyms_list = [word for word in words if word.isupper() and len(word) >= 2]
    
    return acronyms_list

     

def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
