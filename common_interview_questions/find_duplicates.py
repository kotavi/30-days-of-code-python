"""

You need to write a program to find all duplicates in an array
where the numbers in the array are in the range of 0 to n-1 where n is the size of the array.

"""

def find_duplicates(arr,  multiple_duplicate=True):
    """

    :param arr: input array of values in the range of 0 to n-1
    :param multiple_duplicate: True if duplicates are allowed in the result
    :return: list of duplicate values
    """
    res_duplicates = []
    ht = {}
    # loop through the array
    for value in arr:
        if value in ht:
            res_duplicates.append(value)
        else:
            ht[value] = value
    if multiple_duplicate:
        return res_duplicates
    else:
        return list(set(res_duplicates))

print(find_duplicates([1, 3, 4, 2, 3, 1, 4, 4]))
print(find_duplicates([1, 3, 4, 2, 3, 1, 4, 4], False))