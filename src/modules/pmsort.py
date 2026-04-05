"""
pmsort.py
Sequential (stable) merge sort and depth-limited *single-pool* parallel merge sort.
Designed to work on Windows (spawn) by avoiding nested process pools.
"""


import multiprocessing
from . import sorting

def parallel_merge_sort(
    arr: list,
    ascending: bool = True,
    max_depth: int = 2,
    num_workers: int = 2,
    depth: int = 0
) -> list:
    '''Performs parallel merge sort and returns sorted array'''

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
        
    def worker_process(arr, queue, ascending, max_depth, depth):
        ''''''

        queue.put(parallel_merge_sort(arr, ascending, max_depth, num_workers, depth + 1))


    # base case
    if len(arr) <= 1 or depth >= max_depth:
        return sorting.merge_sort(arr, ascending)

    # recursive case
    else:
        mid_index = len(arr) // 2
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]
        left_queue = multiprocessing.Queue()
        right_queue = multiprocessing.Queue()

        # create processes
        processes = list()
        left = (left_arr, left_queue)
        right = (right_arr, right_queue)

        for sub_arr, queue in [left, right]:
            process = multiprocessing.Process(
                target = worker_process,
                args = (sub_arr, queue, ascending, max_depth, depth)
            )
            processes.append(process)
            process.start()

        # waits process finish
        for process in processes:
            process.join()

        # gets process results
        left_result = left_queue.get()
        right_result = right_queue.get()
        sorted_arr = merge_two_sorted_arrays(left_result, right_result, ascending)
        return sorted_arr