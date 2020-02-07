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

str1 = "xxxxyyyyyyxxxxxxyyyyyyyy"
lst = list(str1)
prev = str1[0]
i = 1
while i < len(lst):
    if prev == lst[i]:
        del lst[i]
    else:
        i += 1
        prev = lst[i]
print("".join(lst))
