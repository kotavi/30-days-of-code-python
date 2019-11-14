

str1 = "lkenfaawnjfwnFqnlem;jhgjhfddtrdytuytiuqiwiuwefbiwuefiwehfiehriethksdsmdvmnxvmnsdvmsdvsjkbkjafbkjdbejkwfhwjh"
str_list = []
for s in str1:
    str_list.append(s)

print(str_list)

d = {}
for key in str_list:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1

print(d)

print('\nSorted by key:')
for key in sorted(d.keys()):
    print("{} appears {} time(s)".format(key, d[key]))

print('\nSorted by value:')
for key in sorted(d, key=lambda k: d[k]):
    print("{} appears {} time(s)".format(key, d[key]))