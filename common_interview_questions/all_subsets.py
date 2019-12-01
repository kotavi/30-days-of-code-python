"""
https://coderbyte.com/algorithm/print-all-subsets-given-set

The input for this problem will be an array of numbers representing a set,
which only contains unique numbers, and your goal is to print every possible set combination,
otherwise known as the power set. For example:

input set = [1, 2, 3]
power set = [[], [1], [2], [3], [1, 2], [2, 3], [1, 3] [1, 2, 3]]

The solution:
There will be 2N possible combinations of a set of length N because every element can either be in the set or not,
which gives us 2 possibilities, and we do this for N numbers, giving us 2 * 2 * 2 ... = 2N.

(1) Loop from 0 to 2N
(2) For each number get the binary representation of the number, e.g. 3 = 011
(3) Determine from the binary representation whether or not to include a number from the set,
e.g. 011 = [exclude, include, include]

"""

arr = [1, 3, 4, 5, 7]

# number of all possible positions: 2^n
total = 2**len(arr)
res_lst = []

for i in range(total):
    temp_lst = []
    binary_value = str(bin(i))[2:]

    # fill in first positions with '0'
    for k in range(len(arr)):
        while len(binary_value) <  len(arr):
            binary_value = '0' + binary_value
    # go through binary number, if j-th bit is equal to '1' then j-th element from arr will be included
    # in the output combination
    for j in range(len(binary_value)):
        if binary_value[j] == '1':
            temp_lst.append(arr[j])
    res_lst.append(temp_lst)

print(res_lst)


