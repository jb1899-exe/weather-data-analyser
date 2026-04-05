def merge_two_lists(a: list, b: list) -> list:
    '''Merges list_b into list_a in-place unsorted'''

    new_a = list(a)
    new_b = list(b)

    new_a = [0] * len(new_b)
    for i, val in enumerate(new_b):
        len_diff = len(new_a) - len(new_b)
        new_a[i + len_diff] = val
    return new_a