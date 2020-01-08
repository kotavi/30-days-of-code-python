from collections import Counter
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
def rotate(nums, k=3):
    for i in range(k):
        nums.insert(0, nums.pop())
    return nums

print(rotate([1, 2, 3, 4, 5, 6, 7, 8]))
