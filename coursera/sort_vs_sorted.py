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


