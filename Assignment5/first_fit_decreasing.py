# Mark Griffith

import argparse
import timeit
from first_fit import first_fit


def first_fit_decreasing(obj_list):
    """ Sorts the object list in decreasing order
    and calls the first_fit algorithm using the
    sorted list """

    obj_list.sort(reverse=True)
    first_fit(obj_list)


if __name__ == "__main__":
    pars = argparse.ArgumentParser()
    pars.add_argument("obj_file", help="path to file containing objects")
    args = pars.parse_args()

    with open(args.obj_file) as f:
        lines = f.read().split()

    lines = map(float, lines)
    t = timeit.Timer(lambda: first_fit_decreasing(lines))
    elapsed = t.timeit(number=1)

    with open('plotting/plot_data.txt', 'a') as f:
        print >> f, len(lines), elapsed

    print "Total number of objects =", len(lines)
    print "total elapsed time =", elapsed, "seconds"
