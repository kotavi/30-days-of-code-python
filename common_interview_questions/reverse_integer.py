import math

"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
def reverse_int1(x: int) -> int:
    lst = []
    if x == 0:
        return 0
    if x > 0:
        positive = True
    else:
        positive = False
        x = int(math.fabs(x))
    while x > 0:
        rem = x % 10
        x = x // 10
        lst.append(str(rem))

    result = int("".join(lst))
    if result > 2 ** 31 - 1:
        return 0
    else:
        return result if positive else -result


def reverse_int2(x: int) -> int:
    lst = []
    if x == 0:
        return 0
    if x > 0:
        positive = True
    else:
        positive = False
        x = int(math.fabs(x))
    while x > 0:
        rem = x % 10
        x = x // 10
        lst.append(rem)

    result = 0
    m = 1
    n = len(lst)
    for i in range(n-1,-1,-1):
        result += lst[i] * m
        m = m * 10
    if result > 2 ** 31 - 1:
        return 0
    else:
        return result if positive else -result

print(reverse_int1(123))
print(reverse_int1(-123))
print(reverse_int1(1534236469))
print(reverse_int1(4236469))
print(reverse_int1(0))

print(reverse_int2(123))
print(reverse_int2(-123))
print(reverse_int2(1534236469))
print(reverse_int2(4236469))
print(reverse_int2(0))