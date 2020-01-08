from collections import defaultdict

def remove_duplicates(nums):
    hm = defaultdict()
    n = len(nums)
    i = 0
    stopper = 0
    while stopper < n:
        if nums[i] not in hm:
            hm[nums[i]] = 1
            i += 1
        else:
            nums.remove(nums[i])
        stopper += 1
    return len(nums)

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
