"""
Task:
Find maximum length of consecutive 0’s in a given binary string
"""


def consecutive_zeros(b="001010100000000011100000000000000000"):
    n = 0
    c = 0
    count = []
    while n < len(b):
        if b[n] == '0':
            c += 1
        elif b[n] == '1':
            if c != 0:
                count.append(c)
                c = 0
        n += 1
        if n == len(b):
            count.append(c)
    return count


def consecutive_zeros_2(b="001010100000000011100000000000000000"):
    return max(map(len, b.split('1')))


print(consecutive_zeros())
print(consecutive_zeros_2())
