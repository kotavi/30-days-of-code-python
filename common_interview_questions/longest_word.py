def longest_word_1(string_line):
    words = string_line.split()
    max_length = len(words[0])
    resulting_word = words[0]
    for word in words[1:]:
        if len(word) > max_length:
            max_length = len(word)
            resulting_word = word
    return max_length, resulting_word


def longest_word_2(string_line):
    result = []
    for word in string_line.split():
        result.append([word, len(word)])
    result.sort(key=lambda lst: lst[1])
    return result[-1]

print(longest_word_1("Task: Takes a list of words and returns the length of the longest one"))
print(longest_word_2("Task: Takes a list of words and returns the length of the longest one"))