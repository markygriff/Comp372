''' Mark Griffith '''

from collections import defaultdict

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

    # First we create a dictionary which maps
    # sizes to the subsets
    size_dict = defaultdict(list)
    for subset in subsets:
        size_dict[len(subset)].append(subset)

    # Next, we iterate over the subsets in order
    # of greatest size to smallest size
    sorted(size_dict.keys())
    for size in size_dict.keys()[::-1]:
        # Add each subset to the cover and remove from the
        # subset's elements from uncovered
        for subset in size_dict[size]:
            cover.append(subset)
            # This step takes O(len(subset))
            for elem in subset:
                if elem in uncovered:
                    uncovered.remove(elem)
            if len(uncovered) is 0:
                return cover

    return cover
