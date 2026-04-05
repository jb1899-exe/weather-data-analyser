"""
searching.py
Linear search (all matches) and binary search (all matches) for numeric arrays.
Includes nearest value logic for misses (returns closest value(s) and their indices).
No use of built-in searching helpers like bisect.
"""


def linear_search(arr: list, tar: float, near_miss_coef = 0.5) -> tuple:
    '''
    Iteratively searches array for target and appends matched indices.
    Returns list of indices with values matching target if found.
    If no exact matches found, returns near matches.
    '''

    exact_matched_indices = list()
    near_matched_indices = list()
    for i in range(len(arr)):
        if arr[i] == tar:
            exact_matched_indices.append(i)
        elif (arr[i] >= (tar - near_miss_coef)) and (arr[i] <= (tar + near_miss_coef)):
            near_matched_indices.append(i)

    if exact_matched_indices:
        return (1, exact_matched_indices)
    else:
        return (-1, near_matched_indices)
    

def binary_search(arr, tar, low_index = None, high_index = None):
    '''
    Recursively binary searches array (arr) for target value (tar).
    Returns index if target found (first occurrence).
    Assumes arr is sorted and returns nearest value.
    '''

    def linear_traversal(arr, tar, match_index):
        '''Traverses array either side of match indices for all matched values.'''

        left_index = match_index - 1
        right_index = match_index + 1
        matches_indices = [match_index]

        while right_index < len(arr) and arr[right_index] == tar:
            matches_indices.append(right_index)
            right_index += 1
        while left_index >= 0 and arr[left_index] == tar:
            matches_indices.append(left_index)
            left_index -= 1
        return matches_indices


    # setting values for first recursion
    if low_index is None:
        low_index = 0
    if high_index is None:
        high_index = len(arr) - 1

    # if target not found
    if low_index > high_index:

        # returns for target values out-of-bounds
        if low_index >= len(arr):
            return (-1, [high_index])
        if high_index < 0:
            return (-1, [low_index])
        
        # returs near misses
        diff_low = (arr[low_index] - tar) ** 2
        diff_high = (arr[high_index] - tar) ** 2
        if diff_low < diff_high:
            return (-1, [low_index])
        elif diff_low > diff_high:
            return (-1, [high_index])
        else:
            return (-1, [high_index, low_index])
        
    # checks if value found
    mid_index = (low_index + high_index) // 2
    guess_val = arr[mid_index]

    # base case
    if guess_val == tar:
        # traveses either side of first occurrence of match and returns all match indices
        return (1, linear_traversal(arr, tar, mid_index))
    
    # recursive case
    elif guess_val > tar:
        return binary_search(arr, tar, low_index, mid_index - 1)
    else:
        return binary_search(arr, tar, mid_index + 1, high_index)