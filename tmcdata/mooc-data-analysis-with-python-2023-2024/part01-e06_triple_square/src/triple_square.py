
def triple(x):
    """
    Multiplies the given number by 3 and returns the result.

    Args:
        x (int): The number to be multiplied by 3.

    Returns:
        int: The result of multiplying x by 3.
    """
    # Multiply the given number by 3 and return the result
    tr = x * 3        
    return tr


def square(x: int) -> int:
    """
    Calculate the square of a given number.

    Args:
        x (int): The number to be squared.

    Returns:
        int: The square of the input number.
    """
    sq = x ** 2
    return sq



def main():
    """
    Main function that prints the triple and square of numbers from 1 to 10.
    The loop breaks when the square of a number is greater than its triple.
    """
    # Loop through numbers from 1 to 10
    for i in range(1, 11):
        # Calculate the triple and square of the current number
        t1 = triple(i)
        s1 = square(i)

        # Check if square is greater than triple, if so break the loop
        if s1 > t1:
            break
        else:
            # Print the triple and square of the current number
            print(f"triple({i})=={t1} square({i})=={s1}")

if __name__ == "__main__":
    main()
