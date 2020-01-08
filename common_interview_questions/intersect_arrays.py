"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

"""
from collections import Counter

def intersect_1(nums1, nums2):
        lst = []
        for value in nums1:
            if value in nums2:
                lst.append(value)
                nums2.remove(value)
        return lst

def intersect_2(nums1, nums2):
    c1 = Counter(nums1)
    c2 = Counter(nums2)
    lst = []
    for value in c1:
        if value in c2:
            lst += [value] * min(c1[value], c2[value])
    return lst

print(intersect_1([1,1,2,2,3], [1,2,3,3]))
print(intersect_2([1,1,2,2,3], [1,2,3,3]))
