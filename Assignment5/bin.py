## bin.py - defines the Bin class to be used by the bin packing algorithm

class Bin:
    def __init__(self):
        self.bin_list = []
        self.sum = 0

    def show_bin(self):
        return self.bin_list

    def add(self, obj):
        self.bin_list.append(obj)

    def remove(self, obj):
        self.bin_list.remove(obj)

    def get_sum(self):
        for i in self.bin_list:
            self.sum += i
        return self.sum

