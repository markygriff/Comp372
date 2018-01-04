########################################
# Mark Griffith
#
# Implementation of Bin-Packing algorithm
# using a First-Fit strategy
#
########################################

from bin import Bin


def first_fit(obj_list, size_max):
    """ Creates and returns a list of the
        bins populated with the given objects """

    bin_list = [Bin()]

    for object in obj_list:
        alloc_new_bin = True

        # scan through list of bins until one is found with
        # room to fit the object
        for bin in bin_list:
            if bin.get_sum() + object <= size_max:
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
    for bin in bin_list:
        print bin.get_bin_list()
