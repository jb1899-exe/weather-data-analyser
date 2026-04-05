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

    # TODO: ensure the user is not redirected bakc here, load once then quit
    file_loaded = False
    while not file_loaded:
        filename_input = input('\nPlease enter a filename to load (enter "quit" to exit): ') 
        if filename_input in filepaths:
            data = user_interface.load_data(datapath, filename_input)
            user_interface.user_selection(data, datapath, filepaths, filename_input)
            file_loaded = True
        elif filename_input.lower() in ['q', 'quit']:
            print('Quitting...\n')
            break
        else:
            print('please enter a valid input!\n')


if __name__ == '__main__':
    main()