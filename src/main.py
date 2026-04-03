from .modules import user_interface


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

    user_interface.print_filenames(filepaths)
    while True:
        filename_input = input('\nPlease enter a filename to load (enter "quit" to exit): ')
        if filename_input in filepaths:
            data = user_interface.load_data(datapath, filename_input)

            while True:
                operation_input = input('\nPlease enter an operation (search, sort, merge) (enter "quit" to exit): ').lower()
                if operation_input == 'search':
                    user_interface.prompt_user_searching(data)
                elif operation_input == 'sort':
                    user_interface.prompt_user_sorting(data)
                elif operation_input == 'merge':
                    user_interface.prompt_user_merging(data)
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