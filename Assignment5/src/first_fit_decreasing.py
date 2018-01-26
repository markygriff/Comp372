# Mark Griffith
#
# Implementation of Bin-Packing algorithm using a First-Fit-Decreasing
# heuristic
#

import argparse
import time
from first_fit import first_fit


def first_fit_decreasing(obj_list):
    """ Sorts the object list in decreasing order
    and calls the first_fit algorithm using the
    sorted list.

    Returns the number of bins used. """

    obj_list.sort(reverse=True)
    num_bins = first_fit(obj_list)
    return num_bins


def time_fn( fn, *args, **kwargs ):
    """ Times the given function.

    Returns the elapsed time, and function returns. """

    start = time.clock()
    results = fn( *args, **kwargs )
    end = time.clock()
    return end-start, results


if __name__ == "__main__":
    pars = argparse.ArgumentParser()
    pars.add_argument("obj_file", help="path to file containing objects")
    args = pars.parse_args()

    # read the file data as a list of object sizes
    with open(args.obj_file) as f:
        objects = f.read().split()

    # call the first-fit-decreasing algorithm and time its execution
    objects = map(float, objects)
    elapsed, num_bins = time_fn(first_fit_decreasing, objects)

    # append first-fit-decreasing results to the output file
    with open('../plotting/plot_data.txt', 'a') as f:
        print >> f, len(objects), elapsed

    print "Total number of objects =", len(objects)
    print "Total number of bins used =", num_bins
    print "total elapsed time =", elapsed, "seconds"
