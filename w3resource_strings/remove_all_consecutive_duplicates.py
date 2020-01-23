"""
Remove all consecutive duplicates of a given string
"""
import itertools

str1 = "xxxxyyyyyyxxxxxxyyyyyyyy"

grouped = itertools.groupby(str1)
for group in grouped:
    print(group)
    for grouper in group[1]:
        print(grouper)

result = ""
for i in grouped:
    result += i[0]
print(result)

result = "".join(i for i, _ in itertools.groupby(str1))
print(result)