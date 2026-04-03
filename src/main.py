from .modules import sorting, searching, pmsort
import numbers


def get_head(arr, n):
    '''Returns first n values of array.'''

    return arr[:n]


def print_filenames(filepaths: list):
    '''Prints availible filenames in filepaths'''
    
    print('Availible files: ')
    for filename in filepaths:
        print(f'    `{filename}`')


def get_record_count(data: list):
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
    print(f'    {city_name} [{get_record_count(data)} records]: {get_head(data, 10)}...')
    return data


def prompt_user_searching(data: list) -> None:
    '''Prompts user for choice relating to searching dataset and performs operation.'''

    # TODO: sort before searching!
    while True:
        target_input = float(input('\nPlease enter a target value (enter "quit" to exit): '))
        if isinstance(float(target_input), numbers.Number): # validate target is a number
            search_input = input('\nPlease enter a search algorithm (linear, binary) (enter "quit" to exit): ').lower()
            if search_input == 'linear':
                target_index = searching.linear_search(data, target_input)
                if target_index == -1:
                    print('\nTarget not found!')
                    break
                else:
                    print(f'\nTarget found at index {target_index}!')
                    break
            elif search_input == 'binary':
                target_index = searching.binary_search(data, target_input)
                if target_index == -1:
                    print('\nTarget not found!')
                    break
                else:
                    print(f'\nTarget found at index {target_index}!')
                    break
            elif search_input.lower() in ['q', 'quit']:
                print('Quitting...\n')
                break
            else:
                print('Please enter a valid input!\n')
        else:
            print('Please enter a valid input!\n')


def prompt_user_sorting(data: list) -> None:
    '''Prompts user for choice relating to sorting dataset and performs operation.'''

    while True:
        # add ascending / descending
        ascending_input = input('\nPlease enter ascending or descending (enter "quit" to exit): ').lower()
        if ascending_input in ['ascending', 'descending']:
            
            ascending = True
            if ascending_input == 'descending':
                ascending = False

            sort_input = input('\nPlease enter a search algorithm (bubble, insertion, quick, merge) (enter "quit" to exit): ').lower()
            if sort_input == 'bubble':
                sorting.bubble_sort(data, ascending)
                print(get_head(data, 10))
                break
            elif sort_input == 'insertion':
                sorting.insertion_sort(data, ascending)
                print(get_head(data, 10))
                break
            elif sort_input == 'quick':
                sorting.quick_sort(data, ascending)
                print(get_head(data, 10))
                break
            elif sort_input == 'merge':
                sorting.merge_sort(data, ascending)
                print(get_head(data, 10))
                break
            elif sort_input.lower() in ['q', 'quit']:
                print('Quitting...\n')
                break
            else:
                print('Please enter a valid input!\n')
        else:
            print('Please emter a valid input!\n')


def prompt_user_merging(data: list) -> None:
    '''Prompts user for choice relating to merging dataset and performs operation.'''

    while True:
        merge_input = input('\nPlease enter a dataset to merge (enter "quit" to exit): ').lower()
        print(f'Merging {merge_input}...')
        break


def main() -> None:

    filepaths = [
        'CityA_365.txt',
        'CityB_365.txt',
        'CityC_365.txt',
        'CityA_1460.txt',
        'CityB_1460.txt',
        'CityC_1460.txt',
        'CityN_100000.txt'
    ]
    datapath = 'data/'

    print_filenames(filepaths)
    while True:
        filename_input = input('\nPlease enter a filename to load (enter "quit" to exit): ')
        if filename_input in filepaths:
            data = load_data(datapath, filename_input)

            while True:
                operation_input = input('\nPlease enter an operation (search, sort, merge) (enter "quit" to exit): ').lower()
                if operation_input == 'search':
                    prompt_user_searching(data)
                elif operation_input == 'sort':
                    prompt_user_sorting(data)
                elif operation_input == 'merge':
                    prompt_user_merging(data)
                elif filename_input.lower() in ['q', 'quit']:
                    print('Quitting...\n')
                    break
                else:
                    print('Please enter a valid input!\n')
        
        elif filename_input.lower() in ['q', 'quit']:
            print('Quitting...\n')
            break
        else:
            print('please enter a valid input!\n')


if __name__ == '__main__':
    main()