"""
sorting.py
Manual implementations of Bubble Sort, Insertion Sort, Merge Sort (stable), and Quick Sort.
No use of built-in sorting. Functions return new lists and do not mutate inputs.
"""


# Complexity notes:

def bubble_sort(arr: list, ascending: bool = True) -> None:
    '''
    Performs bubble sort on unsorted array.
    '''
    
    for i in range(len(arr) - 1): # No check for i+1 at last value; i reduces search space
        swap = False
        for j in range(len(arr) - (i + 1)): # Compares values in unsorted array
            if ascending: # 'bubbles-up' smallest or largeset values depending on ascending arg
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] # swaps consecutive values
                    swap = True
            if not ascending:
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap = True
        else:
            # checks for swap once inner loop completes
            if not swap:
                break
    

def insertion_sort(arr: list, ascending: bool = True) -> None:
    '''
    Performs insertion sort on unsorted array.
    '''
    
    for i in range(1, len(arr)):
        j = i
        if ascending:
            while j > 0 and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
        if not ascending:
            while j > 0 and arr[j - 1] < arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
    

def merge_sort(arr: list, ascending: bool = True) -> None:
    '''
    Performs merge sort on an unsorted array.
    '''

    def merge_sorted_arrays(arr, arr_a: list, arr_b: list, ascending: bool) -> None | list:
        '''
        Merges two sorted subarrays into single sorted array.
        '''

        i = 0
        j = 0
        k = 0
        if ascending:
            # compares i'th and j'th value in each arr_a and arr_b, inserts into arr at k
            while i < len(arr_a) and j < len(arr_b):
                if arr_a[i] <= arr_b[j]:
                    arr[k] = arr_a[i]
                    i += 1
                else:
                    arr[k] = arr_b[j]
                    j += 1
                k += 1
            # inserts remaining elements from arr_a and arr_b
            while i < len(arr_a):
                arr[k] = arr_a[i]
                i += 1    
                k += 1
            while j < len(arr_b):
                arr[k] = arr_b[j]
                j += 1
                k += 1
        if not ascending:
            # compares i'th and j'th value in each arr_a and arr_b, inserts into arr at k
            while i < len(arr_a) and j < len(arr_b):
                if arr_a[i] >= arr_b[j]:
                    arr[k] = arr_a[i]
                    i += 1
                else:
                    arr[k] = arr_b[j]
                    j += 1
                k += 1
            # inserts remaining elements from arr_a and arr_b
            while i < len(arr_a):
                arr[k] = arr_a[i]
                i += 1
                k += 1
            while j < len(arr_b):
                arr[k] = arr_b[j]
                j += 1
                k += 1
        
        
    # sorts values
    if len(arr) <= 1: # base case
        return
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left, ascending)
        merge_sort(right, ascending)
        merge_sorted_arrays(arr, left, right, ascending)
        

def quick_sort(arr, start_index = None, end_index = None) -> None:

    def swap_vals(arr, a, b):
        '''Swaps values in-place in arr at indices a and b.'''

        if a != b:
            arr[a], arr[b] = arr[b], arr[a]
    
    def partition(arr, start_index, end_index):
        ''''''

        pivot_index = start_index
        pivot_value = arr[pivot_index]

        left_index = pivot_index + 1
        right_index = end_index
        
        while left_index <= right_index:
            while left_index <= right_index and arr[left_index] <= pivot_value:
                left_index += 1
            while left_index <= right_index and arr[right_index] > pivot_value:
                right_index -= 1
            if left_index < right_index:
                swap_vals(arr, left_index, right_index)
        swap_vals(arr, right_index, pivot_index)
        return right_index


    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(arr) - 1
    if start_index < end_index:
        partition_index = partition(arr, start_index, end_index)
        quick_sort(arr, start_index, partition_index - 1)
        quick_sort(arr, partition_index + 1, end_index)