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
                operation_input = input('\nPlease enter an operation (search, sort, merge): ').lower()
                if operation_input == 'search':
                    print('Searching...')
                    break
                
                elif operation_input == 'sort':
                    print('Sorting...')
                    break
                
                elif operation_input == 'merge':
                    print('Merging...')
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