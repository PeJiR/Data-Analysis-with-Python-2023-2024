#!/usr/bin/env python3

def positive_list(L):
    """
    Returns a list of the elements from the input list L that are greater than 0.
    
    Args:
        L (list): The input list.
        
    Returns:
        list: A new list containing the positive elements from L.
    """
    # Use the filter() function to create a new list with only the elements that
    # satisfy the lambda function condition (x > 0). The lambda function checks
    # if each element of the input list is greater than 0.
    
    return list(filter(lambda x:x>0, L))

def main():
     # Test the positive_list function
    print (positive_list([2,-2,0,1,-7]))
     

if __name__ == "__main__":
    main()
