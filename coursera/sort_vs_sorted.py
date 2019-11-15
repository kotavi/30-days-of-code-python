import math


my_list1 = [-3, 0, 7, 1, -9, 4, 12, 67]
# my_list1.sort() - changes the my_list1 and returns None
print(my_list1.sort())
print(my_list1)
# that's why sort() doest'n work on strings, because strings aren't mutable


my_list2 = [0, -7, -1, -9, 4, 12, 6, 7]
# sorted(my_list1) - doesn't change the my_list1 and returns a new sorted list
print(sorted(my_list2))
my_list3 = sorted(my_list2)
print(my_list3 == my_list2)


# optional key parameters
print(sorted([1,4,0,-5], reverse=True, key=math.fabs))
print(sorted([1,4,0,-5], key=lambda x: math.fabs(x)))


# sort the given list of strings by the second letter
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
def second_let(word):
    return word[1]
func_sort = sorted(ex_lst, key=second_let)

# sort the given list of numbers by the last digit, from highest to lowest
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
nums_sorted_lambda = sorted(nums, reverse=True, key=lambda num: num[-1])


"""
Create a function called last_four that takes in an ID number and returns the last four digits. 
For example, the number 17573005 should return 3005. T
hen, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. 
Save this sorted list in the variable, sorted_ids. 
Hint: Remember that only strings can be indexed, so conversions may be needed.
"""
def last_four(x):
    temp = str(x)[-4:]
    return int(temp)
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key=last_four)
print(sorted_ids)

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key=lambda x: int(str(x)[-4:]))
print(sorted_ids)

