import random
from colorama import Fore, Back, Style
a = []
list_length = 100
print("Creating a list of size 100...")
for i in range(list_length):
    a.append(random.randrange(-100, 100))

print("Original list with positive and negative values:\n{}".format(a))

def filter_negative(element):
    if element > 0:
        return element

def odd_or_even(element):
    if element % 2 == 0:
        return 1
    else:
        return 0

print(Fore.LIGHTMAGENTA_EX + "\n---FILTER function---")
filtered_with_function_a = filter(filter_negative, a)
print(Fore.BLUE + "New list which negative values were filtered out by 'filter_negative' function:\n{}"
      .format(list(filtered_with_function_a)))
filtered_with_lambda_a = filter(lambda x: x > 0, a)
print("New list which negative values were filtered out by lambda function:\n{}"
      .format(list(filtered_with_lambda_a)))
filtered_even_with_lambda_a = filter(lambda x: x % 2 == 0, a)
print("New list which odd values were filtered out by lambda function:\n{}"
      .format(list(filtered_even_with_lambda_a)))

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = list(filter(lambda B_word: 'B' in B_word, countries))
print("Contains the strings from countries that begin with B:\n{}".format(b_countries))


print(Fore.LIGHTMAGENTA_EX + "\n---MAP function---")
odd_or_even_a = map(odd_or_even, a)
print(Fore.BLUE + "New list with 1 and 0, where 1 - even, 0 - odd numbers:\n{}"
      .format(list(odd_or_even_a)))

even_a = map(lambda x: x ** 2, a)
print("New list with numbers in power 2:\n{}".format(list(even_a)))


print(Style.RESET_ALL)
print("-" * 60)
print(Fore.LIGHTRED_EX + """Below, we have provided a list of strings called abbrevs. 
Use map to produce a new list called abbrevs_upper 
that contains all the same strings in upper case.""")
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
abbrevs_upper = list(map(lambda s: s.upper(), abbrevs))
print("Strings in upper case:\n{}".format(abbrevs_upper))

print(Style.RESET_ALL)
print("-" * 60)
print(Fore.LIGHTBLACK_EX + """Write code to assign to the variable filter_testing all the elements in lst_check 
that have a w in them using filter.""")
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing = list(filter(lambda word: 'w' in word, lst_check))
print("Words that have a w in them:\n{}".format(filter_testing))
