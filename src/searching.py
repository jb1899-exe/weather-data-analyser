"""
searching.py
Linear search (all matches) and binary search (all matches) for numeric arrays.
Includes nearest value logic for misses (returns closest value(s) and their indices).
No use of built-in searching helpers like bisect.
"""


def linear_search(arr, tar):
    '''
    Iteratively searches array (arr) for target value (tar). 
    Returns index if target found or -1 if not.
    '''

    # checks each index for target value
    for i in range(len(arr)):
        if arr[i] == tar:
            return i
    # returns if target not found
    else:
        return -1
    

def binary_search(arr, tar, low_index = None, high_index = None):
    '''
    Recursively binary searches array (arr) for target value (tar).
    Returns index if target founf or -1 if not.
    '''

    # setting values for first recursion
    if low_index is None:
        low_index = 0
    if high_index is None:
        high_index = len(arr) - 1

    # if target not found
    if low_index > high_index:
        return - 1
    
    # checks if value found
    mid_index = (low_index + high_index) // 2
    guess_val = arr[mid_index]

    # base case
    if guess_val == tar:
        return mid_index
    
    # recursive case
    elif guess_val > tar:
        return binary_search(arr, tar, low_index, mid_index - 1)
    else:
        return binary_search(arr, tar, mid_index + 1, high_index)