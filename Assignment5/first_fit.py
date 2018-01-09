# Mark Griffith
#
# Implementation of Bin-Packing algorithm using a First-Fit heuristic
#

import argparse
import time
from bin import Bin


def first_fit(obj_list):
    """ Creates a list of bins required to fit the
    given list of objects.

    Returns the number of bins used. """

    # initialize the list of bin objects
    bin_list = [Bin()]

    for object in obj_list:
        alloc_new_bin = True

        # scan through list of bins until one is found with
        # room to fit the object
        for bin in bin_list:
            if bin.get_sum() + object <= 1:
                # allocate object size to the found bin
                bin.add(object)
                alloc_new_bin = False
                break

        # if the object cannot be added to an existing bin
        # create a new bin for the object to be put in
        if alloc_new_bin is True:
            newbin = Bin()
            newbin.add(object)
            bin_list.append(newbin)

    return len(bin_list)



def time_fn( fn, *args, **kwargs ):
    """ Times the given function.

    Returns the elapsed time, and function returns. """

    start = time.clock()
    results = fn( *args, **kwargs )
    end = time.clock()
    return end-start, results


if __name__ == "__main__":
    # parse arguments
    pars = argparse.ArgumentParser()
    pars.add_argument("obj_file", help="path to file containing objects")
    args = pars.parse_args()

    # read the file data as a list of object sizes
    with open(args.obj_file) as f:
        objects = f.read().split()

    # call the first-fit algorithm and time its execution
    objects = map(float, objects)
    elapsed, num_bins = time_fn(first_fit, objects)

    # append first-fit results to the output file
    with open('plotting/plot_data.txt', 'a') as f:
        print >> f, len(objects), elapsed

    print "Total number of objects =", len(objects)
    print "Total number of bins used =", num_bins
    print "Total elapsed time =", elapsed, "seconds"
