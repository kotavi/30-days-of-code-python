"""
Write a Python program to create two strings from a given string.
Create the first string using those character which occurs only once and create the second string which
consists of multi-time occurring characters in the said string.
"""

from collections import Counter

given_string = "aabbcceffgh"
str1 = ""
str2 = ""

given_string_count = Counter(given_string)
for key, value in given_string_count.items():
    if value != 1:
        str1 += key
    else:
        str2 += key

print(str1, str2)
