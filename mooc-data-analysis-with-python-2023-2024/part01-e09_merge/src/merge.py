#!/usr/bin/env python3

def merge(L1, L2):
    """
    Merge two sorted lists L1 and L2 into a new list L in sorted order.

    Args:
    L1 (list): The first list to be merged.
    L2 (list): The second list to be merged.

    Returns:
    list: A new list containing elements from L1 and L2, in sorted order.
    """

    # Initialize an empty list to hold the merged list
    L = []

    # Initialize indices for L1 and L2
    i,j = 0 ,0

    # While there are elements in L1 and L2, merge the smallest one into L
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1

    # Append any remaining elements from L1 (if any) to L
    while i < len(L1):
        L.append(L1[i])
        i += 1

    # Append any remaining elements from L2 (if any) to L
    while j < len(L2):
        L.append(L2[j])
        j += 1

    # Return the merged list
    return L

def main():
    
    L1 = [1, 3, 5, 7]
    L2 = [2, 4, 6, 8]
    merged_list = merge(L1,L2)
    print(merged_list)
    
if __name__ == "__main__":
    main()
