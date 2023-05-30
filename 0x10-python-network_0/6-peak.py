#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    # Get the length of the input list
    n = len(list_of_integers)
    
    # Check if the list is empty
    if n == 0:
        return None
    
    # Initialize the start and end indices
    start = 0
    end = n - 1
    
    # Perform binary search to find a peak
    while start < end:
        # Calculate the mid index
        mid = (start + end) // 2
        
        # Compare the middle element with its neighbors
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid
    
    # Return the peak element
    return list_of_integers[start]


