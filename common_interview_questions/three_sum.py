"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.
"""

def three_sum(nums):

    result = set()
    n = len(nums)
    nums.sort()

    for i in range(n-2):
        j, k = i+1, n-1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                result.add((nums[i], nums[j], nums[k]))
                j += 1
            else:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
    return result

print(three_sum([-1, -2, 3, 0, -2, -9, 9, 5, 4, 1, -7, 10]))
