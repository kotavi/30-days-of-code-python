import math


def squared(number):
    return math.sqrt(number)


def double(number):
    return 2 * number


def minus_one(number):
    return number - 1


def pow_2(number):
    return number * number


functions_list = [
    double,
    minus_one,
    pow_2,
    squared
]

my_number = 3
for func in functions_list:
    my_number = func(my_number)

print(my_number)
