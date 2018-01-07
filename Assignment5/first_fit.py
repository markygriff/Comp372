# Mark Griffith
#
# Implementation of Bin-Packing algorithm
# using a First-Fit strategy
#

import argparse
import timeit
from bin import Bin


def first_fit(obj_list):
    """ Creates and returns a list of the
        bins populated with the given objects """

    bin_list = [Bin()]

    for object in obj_list:
        alloc_new_bin = True

        # scan through list of bins until one is found with
        # room to fit the object
        for bin in bin_list:
            if bin.get_sum() + object <= 1:
                bin.add(object)
                alloc_new_bin = False
                break

        # if object cannot be added to an existing bin
        # create a new bin for the object to be put in
        if alloc_new_bin is True:
            newbin = Bin()
            newbin.add(object)
            bin_list.append(newbin)

    # print items in bins as lists
    # for num, bin in enumerate(bin_list):
        # print "Bin", num, ":", bin.get_bin_list()
    print "Total bins used =", len(bin_list)


if __name__ == "__main__":
    pars = argparse.ArgumentParser()
    pars.add_argument("obj_file", help="path to file containing objects")
    args = pars.parse_args()

    with open(args.obj_file) as f:
        lines = f.read().split()

    lines = map(float, lines)
    t = timeit.Timer(lambda: first_fit(lines))
    elapsed = t.timeit(number=1)

    with open('plotting/plot_data.txt', 'a') as f:
        print >> f, len(lines), elapsed

    print "Total number of objects =", len(lines)
    print "Total elapsed time =", elapsed, "seconds"
