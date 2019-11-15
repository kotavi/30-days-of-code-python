

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


"""
Task: sort the dictionary by the count of cities that start with 'S'
"""
states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}
def count_cities(cities_list, char_):
    count = 0
    for city in cities_list:
        if city[0] == char_:
            count += 1
    return count
print('\nSort the dictionary by the count of cities that start with "S": ')
print(sorted(states, key=lambda state: count_cities(states[state], 'S')))

def count_cities_for_state(state):
    cities_list = states[state]
    return count_cities(cities_list, 'T')
print('\nSort the dictionary by the count of cities that start with "T": ')
print(sorted(states, key=count_cities_for_state))

def count_cities_for_state(state):
    return sum([1 for city in states[state] if city[0] == 'O'])
print('\nSort the dictionary by the count of cities that start with "O": ')
print(sorted(states, key=count_cities_for_state, reverse=True))

print('\nSort the dictionary by the count of cities that start with "O": ')
print(sorted(states, key=lambda state: sum([1 for city in states[state] if city[0] == 'O']), reverse=True))