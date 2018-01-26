# Mark Griffith


class Bin(object):
    """ Bin class to be used with the Bin-Packing alg """
    def __init__(self):
        self.bin_list = []
        self.sum = 0

    def get_bin_list(self):
        """shows the bin list"""
        return self.bin_list

    def add(self, obj):
        """appends object to the bin list"""
        self.bin_list.append(obj)
        self.sum += obj

    def remove(self, obj):
        """removes object from the bin list"""
        self.bin_list.remove(obj)
        self.sum -= obj

    def get_sum(self):
        """returns the sum of the objects
           in the bin list"""
        # for i in self.bin_list:
        #     self.sum += i
        return self.sum
