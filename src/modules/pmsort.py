"""
pmsort.py
Sequential (stable) merge sort and depth-limited *single-pool* parallel merge sort.
Designed to work on Windows (spawn) by avoiding nested process pools.
"""


# TODO: add parallelism
def parallel_merge_sort(arr: list, ascending: bool = True) -> list:
    '''Performs merge sort and returns sorted array'''

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
        left_arr = parallel_merge_sort(arr[:mid_index], ascending)
        right_arr = parallel_merge_sort(arr[mid_index:], ascending)
        sorted_arr = merge_two_sorted_arrays(left_arr, right_arr, ascending)
        return sorted_arr