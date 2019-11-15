from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)


dd = defaultdict(int)
dd['python2'] = 23
dd['something-else'] = 45
dd['python3'] = 30
for i in dd.items():
    print(i)

"""
https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. 
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, print -1.
"""
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d[input()].append(str(i+1))
for i in range(m):
    print(' '.join(map(str, d[input()])) or -1)