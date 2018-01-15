
def GSC(uncovered, subsets):
    ''' This algorithm finds the set cover of Uncovered using a greedy
        heuristic

        Assumes all elements needed to create a cover of Uncovered are
        in Subsets

        Inputs:
            unocovered = set of values to be covered
            subsets = list of subsets to cover Uncovered

        Returns the found list of subsets that form a set cover'''

    cover = []

    # iterate over easch subset and append that subset to the cover
    for i in subsets:
        cover.append(i)
        # Note: this step require O(size of subset i) time
        uncovered = uncovered.difference(i)
        # exit when the full cover has been achieved
        if len(uncovered) is 0:
            return cover

    return cover
