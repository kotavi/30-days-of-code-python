"""
Given: two lists.
Task: create a third list by picking an odd-index element from the first list and even index elements from second.
"""


def combine_by_odd_and_even(lst1, lst2):
    return lst1[1::2] + lst2[0::2]


print(combine_by_odd_and_even([0, 1, 2, 3], [5, 6, 7, 8, 9, 10]))
