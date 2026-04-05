from . import sorting
from . import searching
from . import pmsort
from . import merging
import numbers


def get_head(arr: list, n: int) -> list:
    '''Returns first n values of array.'''

    return arr[:n]


def print_filenames(filepaths: list) -> None:
    '''Prints availible filenames in filepaths'''
    
    print('Availible datasets: ')
    for filename in filepaths:
        print(f'    {filename}')


def get_record_count(data: list) -> int:
    '''Returns length of data.'''

    count = 0
    for _ in data:
        count += 1
    return count


def load_data(datapath: str, filename: str) -> list:
    '''Takes string filepath and returns list of data.'''

    filepath = f'{datapath}{filename}'
    data = list()
    with open(filepath, 'r') as file:
        for i, row in enumerate(file):
            try:
                data.append(float(row.strip()))
            except ValueError:
                print(f'ERROR: Non-numeric found at record: {i}!')
                continue
    city_name = filename[:-8]
    print(f'    Loading {city_name} [{get_record_count(data)} records] - Head (10): {get_head(data, 10)}...')
    return data


def prompt_user_searching(data: list) -> None:
    '''Prompts user for choice relating to searching dataset and performs operation.'''

    #  Default binary search to ascending quick sort
    sorted_data = sorting.quick_sort(data)

    while True:
        # TODO: validate target is a number
        target_input = input('\nPlease enter a target value (enter "quit" to exit): ')
        if isinstance(float(target_input), numbers.Number): 
            search_input = input('\nPlease enter a search algorithm (linear, binary) (enter "quit" to exit): ').lower()
            
            if search_input == 'linear':
                # TODO: correct printing logic
                search_result = searching.linear_search(data, float(target_input))
                print_multiindex(data, search_result)
                break
            
            elif search_input == 'binary':
                search_result = searching.binary_search(sorted_data, float(target_input))
                print_multiindex(data, search_result)
                break
            
            elif search_input.lower() in ['q', 'quit']:
                print('Quitting...\n')
                break
            else:
                print('Please enter a valid input!\n')
        elif target_input.lower() in ['q', 'quit']:
            break
        else:
            print('Please enter a valid input!\n')


def print_multiindex(data, search_output):
    ''''''
    
    if search_output[0] == 1:
        for i in search_output[1]:
            print(f'    Exact match: Index: {i}, Value: {data[i]}')
    if search_output[0] == -1:
        for i in search_output[1]:
            print(f'    Near match: Index: {i}, Value: {data[i]}')


def prompt_user_sorting(data: list, filename: str) -> list:
    '''Prompts user for choice relating to sorting dataset and performs operation.'''

    sorted_data = list(data)
    while True:
        ascending_input = input('\nPlease enter ascending or descending order (enter "quit" to exit): ').lower()
        if ascending_input in ['ascending', 'descending']:
            
            ascending = True
            if ascending_input == 'descending':
                ascending = False

            sort_input = input('\nPlease enter a search algorithm (bubble, insertion, quick, merge, parallel_merge) (enter "quit" to exit): ').lower()
            if sort_input == 'bubble':
                sorted_data = sorting.bubble_sort(sorted_data, ascending)
                print_vals(sorted_data, filename)
                break
            elif sort_input == 'insertion':
                sorted_data = sorting.insertion_sort(sorted_data, ascending)
                print_vals(sorted_data, filename)
                break
            elif sort_input == 'quick':
                sorted_data = sorting.quick_sort(sorted_data, ascending)
                print_vals(sorted_data, filename)
                break
            elif sort_input == 'merge':
                sorted_data = sorting.merge_sort(sorted_data, ascending)
                print_vals(sorted_data, filename)
                break
            elif sort_input == 'parallel_merge':
                sorted_data = pmsort.parallel_merge_sort(sorted_data, ascending)
                print_vals(sorted_data, filename)
                break
            elif sort_input.lower() in ['q', 'quit']:
                print('Quitting...\n')
                break
            else:
                print('Please enter a valid input!\n')

        elif ascending_input.lower() in ['q', 'quit']:
                print('Quitting...\n')
                break
        else:
            print('Please emter a valid input!\n')
    
    return sorted_data


def prompt_user_merging(data: list, datapath, filepaths, filename_input) -> None:
    '''Prompts user for choice relating to merging dataset and performs operation.'''

    while True:
        merge_input = input('\nPlease enter a dataset to merge (enter "quit" to exit): ')
        if merge_input in filepaths:
            new_data = load_data(datapath, f'{merge_input}.txt')
            print_vals(data, filename_input)
            data = merging.merge_two_lists(data, new_data)
            print_vals(new_data, merge_input)
            print(f'\nMerging...')
            break
        elif merge_input.lower() in ['q', 'quit']:
            print('Quitting...\n')
            break
        else:
            print('please enter a valid input!\n')


def get_nth_value(data: list, n: int) -> list:
    '''Gets values in data at n intervals.'''

    output_values = list()
    for i, value in enumerate(data):
        if i % n == 0:
            output_values.append(value)
    return output_values


def print_vals(data: list, filename: str) -> None:
    '''Print values in data at 15 and 100 intervals based on filesize.'''

    if len(data) == 365:
        print(f'    {filename} [Every 15th value]: {get_nth_value(data, 15)}')
    elif len(data) == 1460:
        print(f'    {filename} [Every 100th value]: {get_nth_value(data, 100)}')
    elif len(data) == 100000:
        print(f'    {filename} [Every 100th value]: Head (10): {get_head(get_nth_value(data, 100), 10)}...')


def user_selection(data: list, datapath: str, filepaths: list, filename_input: str) -> None:
    '''Controls user selection of operations.'''

    while True:
        operation_input = input('\nPlease enter an operation (search, sort, merge) (enter "quit" to exit): ').lower()
        if operation_input == 'search':
            prompt_user_searching(data)
        elif operation_input == 'sort':
            prompt_user_sorting(data, filename_input)
        elif operation_input == 'merge':
            prompt_user_merging(data, datapath, filepaths, filename_input)
        elif operation_input.lower() in ['q', 'quit']:
            print('Quitting...\n')
            break
        else:
            print('Please enter a valid input!\n')