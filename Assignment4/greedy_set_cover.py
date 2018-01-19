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

    size_dict = defaultdict(list)
    for s in subsets:
        size_dict[len(s)].append(s)

    # size_dict.keys().sort(reverse=True)
    sorted(size_dict.keys())
    for size in size_dict.keys()[::-1]:
        for s in size_dict[size]:
            cover.append(s)
            for elem in s:
                if elem in uncovered:
                    uncovered.remove(elem)
            if len(uncovered) is 0:
                return cover

    return cover

#     # This creates a dictionary of lists containing
#     # the sets in which each element appears
#     element_locations_dict = defaultdict(list)
#     for n, subset in enumerate(subsets):
#         for element in subset:
#             element_locations_dict[element].append(n)

#     # This creates a dictionary of set sizes mapped to their set
#     set_sizes_dict = defaultdict(set)
#     for n, sub in enumerate(subsets):
#         set_sizes_dict[len(sub)].add(n)

#     cover = []
#     if len(uncovered) is 0:
#         return cover

#     max_subset_size = max(len(s) for s in subsets)
#     for set_size in range(max_subset_size, 0, -1):
#         if set_size in set_sizes_dict:
#             # This is a set of all subsets with size = set_size
#             curr_sized_subsets = set_sizes_dict[set_size]
#             while len(curr_sized_subsets) is not 0:
#                 tmp = curr_sized_subsets.pop()
#                 cover.append(tmp)
#                 # Look through elements in the added subset
#                 for i in subsets[tmp]:
#                     # Look through sets which contain that element
#                     for j in element_locations_dict[i]:
#                         if j != tmp:
#                             # Remove instances of the elements added
#                             # to the cover in other sets
#                             s = subsets[j]
#                             set_sizes_dict[len(s)].remove(j)
#                             s.remove(i)
#                             set_sizes_dict[len(s)].add(j)

#     return cover



#     cover = []

#     # iterate over easch subset and append that subset to the cover
#     for i in subsets:
#         cover.append(i)
#         # Note: this step require O(size of subset i) time
#         uncovered = uncovered.difference(i)
#         # exit when the full cover has been achieved
#         if len(uncovered) is 0:
#             return cover

#     return cover
