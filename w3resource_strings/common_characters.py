"""
Find all the common characters in lexicographical order from two given lower case strings.
If there are no common letters print "No common characters".
"""
from collections import Counter

def common_characters(str1, str2):
    c1 = Counter(str1)
    c2 = Counter(str2)

    common = c1 & c2
    if not common:
        return "No common characters."

    return "".join(common.keys())

print(common_characters("Python", "Print"))