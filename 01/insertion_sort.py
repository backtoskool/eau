#!/usr/bin/python3


def insertion_sort(lst):
    """ Sort list using the InsertionSort algorithm.

    >>> insertion_sort([24, 6, 12, 32, 18])
    [6, 12, 18, 24, 32]

    >>> insertion_sort([])
    []

    >>> insertion_sort("hallo")
    Traceback (most recent call last):
        ...
    TypeError: lst must be a list

    """
    if not type(lst) == list:
        raise TypeError('lst must be a list')

    for i in range(1, len(lst)):
        v = lst[i]
        j = i - 1
        while j >= 0 and v < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = v

    return lst


if __name__ == "__main__":
    numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9]
    print(insertion_sort(numbers))
