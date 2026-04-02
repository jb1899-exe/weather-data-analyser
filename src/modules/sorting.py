"""
sorting.py
Manual implementations of Bubble Sort, Insertion Sort, Merge Sort (stable), and Quick Sort.
No use of built-in sorting. Functions return new lists and do not mutate inputs.
"""


# Complexity notes:

def bubble_sort(arr: list, ascending: bool = True, in_place: bool = False) -> None | list:
    '''
    Performs bubble sort on unsorted array.
    '''
    
    if in_place:
        for i in range(len(arr) - 1): # No check for i+1 at last value; i reduces search space
            swap = False
            for j in range(len(arr) - (i + 1)): # Compares values in unsorted array
                if ascending: # 'bubbles-up' smallest or largeset values depending on ascending arg
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j] # swaps consecutive values
                        swap = True
                else:
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swap = True
            else:
                # checks for swap once inner loop completes
                if not swap:
                    break
    else:
        sorted_arr = list(arr)
        for i in range(len(sorted_arr) - 1):
            swap = False
            for j in range(len(sorted_arr) - (i + 1)):
                if ascending:
                    if sorted_arr[j] > sorted_arr[j + 1]:
                        sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                        swap = True
                else:
                    if sorted_arr[j] < sorted_arr[j + 1]:
                        sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                        swap = True
            else:
                if not swap:
                    break
        return sorted_arr
    

def insertion_sort(arr: list, ascending: bool = True, in_place: bool = False) -> None | list:
    '''
    Performs insertion sort on unsorted array.
    '''
    
    if in_place:
        for i in range(1, len(arr)):
            j = i
            if ascending:
                while j > 0 and arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
                    j -= 1
            else:
                while j > 0 and arr[j - 1] < arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
                    j -= 1
    else:
        sorted_arr = list(arr)
        for i in range(1, len(sorted_arr)):
            j = i
            if ascending:
                while j > 0 and sorted_arr[j - 1] > sorted_arr[j]:
                    sorted_arr[j - 1], sorted_arr[j] = sorted_arr[j], sorted_arr[j - 1]
                    j -= 1
            else:
                while j > 0 and sorted_arr[j - 1] < sorted_arr[j]:
                    sorted_arr[j - 1], sorted_arr[j] = sorted_arr[j], sorted_arr[j - 1]
                    j -= 1
        return sorted_arr
    

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
        

def quick_sort(arr, start_index = None, end_index = None):

    def swap_vals(arr, a, b):
        '''Swaps values in-place in arr at indices a and b.'''

        if a != b:
            arr[a], arr[b] = arr[b], arr[a]
    
    def partition(arr, start_index, end_index):
        pivot_index = start_index
        pivot_value = arr[pivot_index]
        start_index = pivot_index + 1
        end_index = len(arr) - 1
        while start_index < end_index:
            while start_index < len(arr) and arr[start_index] <= pivot_value:
                start_index += 1
            while arr[end_index] > pivot_value:
                end_index -= 1
            if start_index < end_index:
                swap_vals(arr, start_index, end_index)
        swap_vals(arr, end_index, pivot_index)
        return end_index

    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(arr) - 1
    if start_index < end_index:
        partition_index = partition(arr, start_index, end_index)
        quick_sort(arr, start_index, partition_index - 1)
        quick_sort(arr, partition_index + 1, end_index)