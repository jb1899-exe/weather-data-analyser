def get_head(arr, n):
    '''Returns first n values of array.'''

    return arr[:n]


def get_filename():
    pass


def get_record_count(data: list):
    '''Returns length of data.'''

    count = 0
    for _ in data:
        count += 1
    return count


def load_data(filepath: str) -> list:
    '''Takes string filepath and returns list of data.'''

    data = list()
    with open(filepath, 'r') as file:
        for i, row in enumerate(file):
            try:
                data.append(float(row.strip()))
            except ValueError:
                print(f'ERROR: Non-numeric found at record: {i}!')
                continue
    return data


def main() -> None:

    # allow user to select wich data to analyse?
    filepaths = [
        'CityA_365.txt',
        'CityB_365.txt',
        'CityC_365.txt'
    ]
    datapath = 'data/'

    data_store = dict()
    print('loading data...')
    for filepath in filepaths:
        city_name = filepath[:-8]
        data = load_data(f'{datapath}{filepath}')
        data_store[city_name] = data
        print(f'    {city_name} [{get_record_count(data)} records]: {get_head(data, 10)}...')




    while True:
        operation_input = input()


if __name__ == '__main__':
    main()