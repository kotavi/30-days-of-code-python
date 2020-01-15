import string

"""
Task 1:
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
"""


def add_ing(word):
    if len(word) > 2:
        if word[-3:] != 'ing':
            word += 'ing'
        elif word[-3:] == 'ing':
            word += 'ly'
    return word


print(add_ing('abc'))
print(add_ing('string'))
print(add_ing('hi'))

"""
Task 2:
Write a Python program to find the first appearance of the substring 'not' and 'poor' 
from a given string, if 'poor' follows the 'not', replace the whole 'not'...'poor' 
substring with 'good'. Return the resulting string.
"""


def find_substring(sample_str="The lyrics is not that poor!"):
    index_not = sample_str.find('not')
    index_poor = sample_str.find('poor')
    res = ""
    if index_not < index_poor:
        res = sample_str.replace(sample_str[index_not:index_poor + len('poor')], 'good')

    return res


print(find_substring())

"""
Task 3:
Remove the characters which have odd index values of a given string. 
"""
sample_string = "resulting"
print(sample_string[1::2])

"""
Task 4:
Count the occurrences of each word in a given sentence.
"""


def count_occurrences(sentence):
    ht = {}
    for word in sentence.split():
            if word in ht:
                ht[word] += 1
            else:
                ht[word] = 1
    return ht


print(count_occurrences("Count the occurrences of each word in a given sentence."))

"""
Task 5:
Create the HTML string with tags around the word(s).
"""


def html_string(sample_string, tag):
    html_tag_start = "<{}>".format(tag)
    html_tag_end = "</{}>".format(tag)
    return html_tag_start + sample_string + html_tag_end


print(html_string('Python', 'i'))
print(html_string('Python Tutorial', 'b'))

"""
Task 6:
Remove duplicate characters of a given string
"""


def remove_duplicate(sample_string="Remove duplicate characters of a given string"):
    ht = {}
    new_string = ""
    for i in range(len(sample_string)):
        if sample_string[i] not in ht:
            new_string += sample_string[i]
            ht[sample_string[i]] = 1
    return new_string


print(remove_duplicate())