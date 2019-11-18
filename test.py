#!/bin/python3
"""
Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in 0's binary representation.

"""

def to_binary(number):
    """

    :param number: integer number
    :return: a list of 1's and 0's representing a binary number
    """
    lst = []
    while number > 0:
        lst.append(number % 2)
        number = number // 2
    lst.reverse()
    return lst

def consecutive_count(lst):
    """

    :param lst: list of 1's and 0's
    :return: a maximum number of consecutive 1's
    """
    count, max_count = 0, 0
    for v in lst:
        if v == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

def fill_with_zeros(lst, size):
    """

    :param lst: list of 1's and 0's
    :param size: expected size of the list
    :return: a new list where first positions are filled with 0's
    """
    old_size = len(lst)
    if size == old_size:
        return lst
    new_lst = []
    for i in range(size - old_size):
        new_lst.append(0)
    new_lst += lst
    return new_lst


def binary_sum(a, b, binary=False):
    """

    :param a: first integer number
    :param b: second integer number
    :param binary: type of numbers representation
    :return: result of binary sum of a and b
    """

    if not binary:
        lst_a, lst_b = to_binary(a), to_binary(b)
    else:
        lst_a, lst_b = a, b
    max_size = max(len(lst_a), len(lst_b))
    memory = 0
    result = ''
    lst_a = fill_with_zeros(lst_a, max_size)
    lst_b = fill_with_zeros(lst_b, max_size)
    for i in range(max_size-1, -1, -1):
        s = lst_a[i] + lst_b[i]
        if s == 2: # 1+1
            if memory == 0:
                memory = 1
                result = '0' + result
            else:
                result = '1' + result
        elif s == 1: # 1+0
            if memory == 0:
                result = '1' + result
            else:
                result = '0' + result
        else: # 0+0
            if memory == 0:
                result = '0' + result
            else:
                result = '1' + result
                memory = 0
    if memory == 1:
        result = '1' + result
    return result


def from_binary(b_number):
    """

    :param b_number: binary number, for example: 11100
    :return: integer number
    """
    str_number = ''
    if type(b_number) is list:
        for v in b_number:
            str_number = str_number + str(v)
    else:
        str_number = str(b_number)
    result = 0
    k = 0
    i = len(str_number) - 1
    while i >= 0:
        result += 2 ** k * int(str_number[i])
        k += 1
        i -= 1
    return result

def inverse(lst):
    """

    :param lst: list of 1's and 0's
    :return: flipped list
    """
    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = 1
        else:
            lst[i] = 0
    return lst

def negative_binary_number(number):
    # convert to binary
    binary_number = to_binary(number)
    # flip the bits
    flipped_lst = inverse(binary_number)
    # extending the sign
    extended_list = fill_with_zeros(flipped_lst, 8)
    return binary_sum(flipped_lst, [1], True)

if __name__ == '__main__':
    print(binary_sum(from_binary(negative_binary_number(12)), 2)) # ?????????? -12 + 2 in binary
    n = int(input("Enter a base-2 number: "))
    print("{} in binary: {}".format(n, from_binary(n)))
    n = int(input("Enter a base-10 integer: "))
    lst = to_binary(n)
    message = "{} converted to binary: {}".format(n, lst)
    print(message)
    print("The maximum number of consecutive 1's: ", consecutive_count(lst))
    print("*" * len(message))
    print("Binary sum of {} and {}: {}".format(n, 7, binary_sum(n, 7)))
