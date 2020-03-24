import json
from collections import Counter, defaultdict

# read file
with open('words.json', 'r') as fp:
    data = fp.read()

words_dict = json.loads(data)
words_dict_by_len = defaultdict(list)

# separate words into classes of words with the same length and sort each word
for key, words in words_dict.items():
    for word in words:
        if word not in words_dict_by_len[len(word)] and len(word) > 1:
            words_dict_by_len[len(word)].append(''.join(sorted(word)))
print(words_dict_by_len)

anagrams = []
for _, words in words_dict_by_len.items():
    for i in range(len(words)-1):
        if words[i] in words[i+1:]:
            anagrams.append(words[i])
print(anagrams)
print(len(anagrams))
