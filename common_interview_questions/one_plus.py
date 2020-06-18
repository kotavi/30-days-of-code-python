"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [1,2,9]
Output: [1,3,0]
Explanation: The array represents the integer 130.

Example 3:
Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The array represents the integer 1000.
"""


# Naive solution
def one_plus_method1(digits):
    if not digits:
        return []
    s = ""
    for value in digits:
        s += str(value)
    new_digit = str(int(s) + 1)
    return [int(value) for value in new_digit]


print(one_plus_method1([]))
print(one_plus_method1([1, 1, 1]))
print(one_plus_method1([1, 9, 9]))
print(one_plus_method1([9, 9, 9]))


"""
            -1
[9, 9,  9,  9]
            +1
            10
        -2
[9  9   9   0]
        +1
        10
    -3
[9  9   0   0]
    +1
    10
-4   
[9  0   0   0]
+1
10
0

[1  0  0   0   0]

-5
"""


def one_plus_method2(digits, end=-1):
    """Recursive way of solving the task"""
    if end == -(len(digits) + 1):
        digits.insert(0, 1)
    else:
        digits[end] += 1
        if digits[end] == 10:
            digits[end] = 0
            one_plus_method2(digits, end - 1)
    return digits


print(one_plus_method2([]))
print(one_plus_method1([1, 1, 1]))
print(one_plus_method1([1, 9, 9]))
print(one_plus_method1([9, 9, 9]))
