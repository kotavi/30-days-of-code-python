"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""
from collections import Counter

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

x = [el for el in nums1 if el in nums2]
print(x)


def intersect_1(nums1, nums2):
    lst = []
    for value in nums1:
        if value in nums2:
            lst.append(value)
            nums2.remove(value)
        if not nums2:
            return lst
    return lst


def intersect_2(nums1, nums2):
    c1 = Counter(nums1)
    c2 = Counter(nums2)
    lst = []
    for key in c1:
        if key in c2:
            lst += [key] * min(c1[key], c2[key])
    return lst


print(intersect_1([1, 1, 2, 2, 3], [1, 2, 3, 3]))
print(intersect_2([1, 1, 2, 2, 3], [1, 2, 3, 3]))
