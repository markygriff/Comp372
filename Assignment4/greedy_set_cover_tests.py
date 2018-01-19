from greedy_set_cover import GSC


def worst_case_test():
    ''' Test worst case when GSC must check all subsets for cover '''
    uncovered = set([1, 3, 5, 7])
    subs = [set([1]), set([3]), set([5]), set([7])]
    res = GSC(uncovered, subs)
    if res == subs:
        print "WORST CASE TEST : PASS\n"
    else:
        print "WORST CASE TEST : FAIL\n", "Got ", res, "\n", "Expected", \
                subs, "\n"


def optimal_test():
    ''' Test if GSC returns the optimal cover '''
    uncovered = set([2, 4, 6, 8, 10, 12])
    subs = [set([4, 8]), set([2, 4, 8, 12]), set([6, 8, 10])]
    res = GSC(uncovered, subs)
    if res == [set([2, 4, 8, 12]), set([6, 8, 10])]:
        print "OPTIMAL CASE TEST : PASS\n"
    else:
        print "OPTIMAL CASE TEST : FAIL\n", "Got ", res, "\n", "Expected", \
                [set([2, 4, 8, 12]), set([6, 8, 10])], "\n"


def empty_test():
    ''' Test if GSC returns an empty set '''
    uncovered = set()
    subs = []
    res = GSC(uncovered, subs)
    if len(res) is 0:
        print "EMPTY TEST : PASS"
    else:
        print "EMPTY TEST : FAIL"


if __name__ == '__main__':
    # Run all tests
    worst_case_test()
    optimal_test()
    empty_test()
