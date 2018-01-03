from bin import Bin

if __name__ == "__main__":
    b = Bin()
    b.add(1)
    b.add(2)
    b.remove(1)
    print(b.get_sum())
    print b.show_bin()

    print "yellow"
