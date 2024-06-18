#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    results = []
    with open(filename,"r")as file:
        next(file)        
        
        for line in file:            
            regex_pattern = (
                r"(\s*\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.+)"  # (\w+|\w+\s+\w+)
            )
            regex_matches = re.match(regex_pattern, line)
            regex_matches = regex_matches.groups()
            regex_matches = f"{regex_matches[0]}\t{regex_matches[1]}\t{regex_matches[2]}\t{regex_matches[3]}"
            results.append(regex_matches)
            
    
    
    
    return results  


def main():
    print(red_green_blue(filename="src/rgb.txt"))

if __name__ == "__main__":
    main()
