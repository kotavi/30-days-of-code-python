"""
Given a smaller string s and a bigger string b, design an algorithm to find all permutations
of the shorter string within the longer one.
Print the location of each permutation
"""
from collections import Counter


def approach1(s='abbc', b='cbabadcbbabbcbabaabccbabc'):
    s_len = len(s)
    s_elements = Counter(s)
    for i in range(len(b) - s_len + 1):
        b_elements = Counter(b[i:s_len+i])
        if s_elements == b_elements:
            print("result: ", b[i:s_len+i])


approach1()

c = Counter('cbabadcbbabbcbabaabccbabc')
print(c)
for k, v in c.items():
    print(k, c[k])

