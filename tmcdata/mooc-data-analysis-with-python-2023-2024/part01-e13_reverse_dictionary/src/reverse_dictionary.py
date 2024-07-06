#!/usr/bin/env python3

def reverse_dictionary(d):
    """
    Reverses a dictionary where the keys represent English words and the values represent Finnish words.
    
    Args:
        d (dict): A dictionary with English words as keys and Finnish words as values.
    
    Returns:
        dict: A new dictionary where the Finnish words are keys and the English words are values.
    """
    
    # Initialize an empty dictionary to store the reversed dictionary
    reverse_d = {}
    
    # Iterate over each key-value pair in the input dictionary
    for eng_word, finn_words in d.items():
        # Iterate over each Finnish word associated with the English word
        for finn_word in finn_words:
            # If the Finnish word is not already a key in the reversed dictionary
            if finn_word not in reverse_d:
                # Add the Finnish word as a key with the English word as the value
                reverse_d[finn_word] = [eng_word]
            else:
                # If the Finnish word is already a key, append the English word to the value list
                reverse_d[finn_word].append(eng_word)
    
    # Return the reversed dictionary
    return reverse_d





def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
