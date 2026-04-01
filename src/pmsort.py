"""
pmsort.py
Sequential (stable) merge sort and depth-limited *single-pool* parallel merge sort.
Designed to work on Windows (spawn) by avoiding nested process pools.
"""


def merge_sort(arr: list, ascending: bool = True) -> list:
    '''
    Performs merge sort on an unsorted array.
    '''

    def merge_sorted_arrays(arr_a: list, arr_b: list, ascending: bool) -> list:
        '''
        Merges two sorted subarrays into single sorted array.
        '''

        sorted_arr = list()
        i = 0
        j = 0
        if ascending:
            # compares i'th and j'th value in each arr_a and arr_b, appends smaller value
            while i < len(arr_a) and j < len(arr_b):
                if arr_a[i] <= arr_b[j]:
                    sorted_arr.append(arr_a[i])
                    i += 1
                else:
                    sorted_arr.append(arr_b[j])
                    j += 1
            # adds remaining elements from arr_a and arr_b to sorted_arr
            while i < len(arr_a):
                sorted_arr.append(arr_a[i])
                i += 1
            while j < len(arr_b):
                sorted_arr.append(arr_b[j])
                j += 1
            return sorted_arr

        if not ascending:
            # compares i'th and j'th value in each arr_a and arr_b, appends smaller value
            while i < len(arr_a) and j < len(arr_b):
                if arr_a[i] >= arr_b[j]:
                    sorted_arr.append(arr_a[i])
                    i += 1
                else:
                    sorted_arr.append(arr_b[j])
                    j += 1
            # adds remaining elements from arr_a and arr_b to sorted_arr
            while i < len(arr_a):
                sorted_arr.append(arr_a[i])
                i += 1
            while j < len(arr_b):
                sorted_arr.append(arr_b[j])
                j += 1
            return sorted_arr
        
        
    # sorts values
    if len(arr) <= 1: # base case
        return arr
    else: # recursive case
        mid = len(arr) // 2
        left = merge_sort(arr[:mid], ascending)
        right = merge_sort(arr[mid:], ascending)
        if left is not None and right is not None:
            sorted_arr = merge_sorted_arrays(left, right, ascending)
            return sorted_arr