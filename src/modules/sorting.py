"""
sorting.py
Manual implementations of Bubble Sort, Insertion Sort, Merge Sort (stable), and Quick Sort.
No use of built-in sorting. Functions return new lists and do not mutate inputs.
"""


def bubble_sort(arr: list, ascending: bool = True) -> list:
    '''Performs bubble sort on unsorted array. Returns new sorted array.'''
    
    new_arr = list(arr)
    for i in range(len(new_arr) - 1): # No check for i+1 at last value; i reduces search space
        swap = False
        for j in range(len(new_arr) - (i + 1)): # Compares values in unsorted array
            if ascending: # 'bubbles-up' smallest or largest values depending on ascending arg
                if new_arr[j] > new_arr[j + 1]:
                    new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j] # swaps consecutive values
                    swap = True
            if not ascending:
                if new_arr[j] < new_arr[j + 1]:
                    new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
                    swap = True
        else:
            # checks for swap once inner loop completes
            if not swap:
                break
    return new_arr

    # Complexity notes:
    # Bubble sort iterates through i'th elements in an array, for each element
    # is compared against j'th other elements and the largest values 'bubble'
    # towards the end. The nested loop structure creates j iterations for each
    # i iteration, and so i * j (or n * n -> O(n^2); This is a quadratic runtime
    # in the worst case when array is unsorted. If the array is already sorted
    # no swaps will be made and the runtime will be O(n). Typically, this is 
    # an instantaneous memory complexity O(1) as elements are swapped in-place, 
    # requiring no extra space for new arrays or temporary elements. Above
    # implementation creates a duplicate array and sorts it, returning sorted
    # array with memory complexity of O(n).
    

def insertion_sort(arr: list, ascending: bool = True) -> list:
    '''Performs insertion sort on unsorted array. Returns new sorted array.'''
    
    new_arr = list(arr)
    for i in range(1, len(new_arr)):
        j = i
        if ascending:
            while j > 0 and new_arr[j - 1] > new_arr[j]:
                new_arr[j - 1], new_arr[j] = new_arr[j], new_arr[j - 1]
                j -= 1
        if not ascending:
            while j > 0 and new_arr[j - 1] < new_arr[j]:
                new_arr[j - 1], new_arr[j] = new_arr[j], new_arr[j - 1]
                j -= 1
    return new_arr

    # Complexity notes:
    # Insertion sort iterates through i'th elements in an array, each element j
    # is then compared sequntially to its neighbour and inserted towards end until
    # it is larger than it's neighbour. Coring j'th elements for each i'th element
    # creates a nested loop (or n * n -> O(n^2); This is a quadratic runtime. Like
    # bubble sort, the time complexity is O(n) for a sorted array. Practically, 
    # insertion sort typically performs better than bubble sort as it only inserts
    # value once correct sorted positoin is found rather than repeatedly 'bubbling'.
    # Memory complecity is O(1) because sorting is performed in-place, no additional
    # arrays or temporary values are required.
    

def merge_sort(arr: list, ascending: bool = True) -> list:
    '''Performs merge sort and returns sorted array.'''

    def merge_two_sorted_arrays(a: list, b: list, ascending: bool):
        '''Merges sorted arrays a and b and returns single array'''

        i = 0
        j = 0
        if ascending:
            sorted_arr = list()
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    sorted_arr.append(a[i])
                    i += 1
                else:
                    sorted_arr.append(b[j])
                    j += 1
            # adds remaining elements from a/b to arr
            while i < len(a):
                sorted_arr.append(a[i])
                i += 1
            while j < len(b):
                sorted_arr.append(b[j])
                j += 1
            return sorted_arr
        if not ascending:
            sorted_arr = list()
            while i < len(a) and j < len(b):
                if a[i] > b[j]:
                    sorted_arr.append(a[i])
                    i += 1
                else:
                    sorted_arr.append(b[j])
                    j += 1
            # adds remaining elements from a/b to arr
            while i < len(a):
                sorted_arr.append(a[i])
                i += 1
            while j < len(b):
                sorted_arr.append(b[j])
                j += 1
            return sorted_arr

    # base case
    if len(arr) <= 1:
        return arr
    # recursive case
    else:
        mid_index = len(arr) // 2
        left_arr = merge_sort(arr[:mid_index], ascending)
        right_arr = merge_sort(arr[mid_index:], ascending)
        sorted_arr = merge_two_sorted_arrays(left_arr, right_arr, ascending)
        return sorted_arr

    # Complexity notes:
    # Merge sort splits the array in half recursively until arrays consist of
    # individual values. Since the problem is halved each iteration, the
    # 'divide' setp of merge sort is logarithmic O(log n). The 'conquer' step
    # requires O(n) time to merge all subarrays at each level of recursion.
    # log n levels of halving and n levels of merging creates an overall
    # runtime of  n * log n = O(n log n) 
        

def quick_sort(arr: list, start_index: int | None = None, end_index: int | None = None, ascending: bool =True) -> list:
    '''Performs quick sort and returns sorted array in ascending or descending order.'''

    # make copy of array 
    new_arr = list(arr)

    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(new_arr) - 1
    if start_index >= end_index:
        return list(new_arr)

    # select approximately middle pivot
    pivot_index = (start_index + end_index) // 2
    pivot_value = new_arr[pivot_index]
    left_arr = list()
    right_arr = list()
    for i in range(start_index, end_index + 1):
        if i == pivot_index:
            continue
        # add logic for ascending and descenging 
        if ascending:
            if new_arr[i] <= pivot_value:
                left_arr.append(new_arr[i])
            else:
                right_arr.append(new_arr[i])
        if not ascending:
            if new_arr[i] >= pivot_value:
                left_arr.append(new_arr[i])
            else:
                right_arr.append(new_arr[i])

    left_arr_sorted = quick_sort(left_arr, 0, len(left_arr) - 1, ascending)
    right_arr_sorted = quick_sort(right_arr, 0, len(right_arr) - 1, ascending)
    sorted_arr =  left_arr_sorted + [pivot_value] + right_arr_sorted
    return sorted_arr

    # Complexity notes:
    # The time complexity of quicksort depends largely on the choice of pivot
    # value. Best performance is achieved when the pivot approximately divides
    # subarrays in half, this yields a best case of O(n log n). Partitioning
    # is linear O(n) while dividing subarrays approximately halves the problem
    # space each iteration O(log n); Together this yields n * log n = n log n.
    # In the worst case, the subarrays are imbalanced and very large or very
    # small pivots are chosen, resulting in closer to O(n) runtime for division
    # for n iterations; This yields n * n = n^2 or O(n^2) quadratic runtime.
    # In short, the further from halving the pivot is, the closer to n steps,
    # the close to halving the pivot is, the closer to log n steps. This is 
    # multiplied by n iterations.