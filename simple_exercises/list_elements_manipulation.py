"""
Given: a list.
Task: remove the element at index 4, add it to the 2nd position and also, at the end of the list
"""

lst = [23, 34, 45, 78, 12, 55, 90]
element = lst.pop(4)
lst.insert(2, element)
# lst.insert(len(lst), element)
lst.append(element)
print(lst)