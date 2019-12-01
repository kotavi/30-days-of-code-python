"""
The challenge is to find all the pairs of two integers in an unsorted array that sum up to a given S.

For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7,
your program should return [[11, -4], [2, 5]]
because 11 + -4 = 7 and 2 + 5 = 7.
"""

arr = [3, 5, 0, -1, 8, 21, -14, 2, 4, 13]
s = 7

print("O(n^2) solution:")
sums1 = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == s:
            sums1.append([arr[i], arr[j]])
print(sums1)

print("\nO(n) solution:")
d = {}
sums2 = []
for value in arr:
    diff = s - value
    if diff not in d:
        d[value] = value
    if diff in d:
        sums2.append([diff, value])
print(sums2)

