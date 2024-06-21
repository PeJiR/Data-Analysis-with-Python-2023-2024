#!/usr/bin/env python3

def file_extensions(filename):
    """
    Reads a file containing a list of filenames. Returns a tuple.
    The first element of the tuple is a list of filenames without extensions,
    and the second element is a dictionary where the keys are the extensions
    and the values are lists of filenames with that extension.

    :param filename: The name of the file containing the list of filenames
    :type filename: str
    """
    
    extensions = {}
    name = []
    
    with open(filename, "r") as file:
        for line in file:
            filename = line.strip()
            if "." not in filename:
                name.append(filename)
            else:
                # Split the filename by the '.' character to get the extension
                parts = filename.split(".")
                # The last element of the list is the extension
                ext = parts[-1]
                if ext in extensions:
                    # If the extension is already in the dictionary, append the filename to the list
                    extensions[ext].append(filename)
                else:
                    # Otherwise add the extension to the dictionary with the filename as the value
                    extensions[ext] = [filename]
       
    return name, extensions

def main():
    """
    Executes the main function of the program.

    This function reads a file containing a list of filenames and calculates the number of files with no extension and the number of files with each extension. It then prints the number of files with no extension and the number of files with each extension.

    Parameters:
    None

    Returns:
    None
    """
    filenames = "src/filenames.txt"
    name,extensions = file_extensions(filenames)
    
    print(f"{len(name)} files with no extension")
    for ext in sorted(extensions.keys()):
        print(f"{ext}: {len(extensions[ext])}")
      

if __name__ == "__main__":
    main()
