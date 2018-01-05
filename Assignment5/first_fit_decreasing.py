# Mark Griffith

from first_fit import first_fit


def first_fit_decreasing(obj_list, size_max):
    """ Sorts the object list and calls the
    first_fit algorithm using the sorted list """

    obj_list.sort(reverse=True)
    first_fit(obj_list, size_max)
