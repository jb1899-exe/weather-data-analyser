from .modules import user_interface


def main() -> None:

    filepaths = [
        'CityA_365',
        'CityB_365',
        'CityC_365',
        'CityA_1460',
        'CityB_1460',
        'CityC_1460',
        'CityN_100000'
    ]
    datapath = 'data/'

    user_interface.print_filenames(filepaths)

    file_loaded = False
    while not file_loaded:
        filename_input = input('\nPlease enter a dataset to load (enter "quit" to exit): ')
        if filename_input in filepaths:
            filename = f'{filename_input}.txt'
            data = user_interface.load_data(datapath, filename)
            user_interface.user_selection(data, datapath, filepaths, filename)
            file_loaded = True
        elif filename_input.lower() in ['q', 'quit']:
            print('Quitting...\n')
            break
        else:
            print('please enter a valid input!\n')


if __name__ == '__main__':
    main()