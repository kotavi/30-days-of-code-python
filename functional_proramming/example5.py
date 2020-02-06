def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def combine_2_and_3(func):
    return func(2, 3)

print(combine_2_and_3(add))
print(combine_2_and_3(subtract))
print(combine_2_and_3(max))
print(combine_2_and_3(min))
print(combine_2_and_3(pow))


def combine_names(func):
    return func('Tetiana', 'Korchak')

def append_with_space(firstname, lastname):
    return f"{firstname} {lastname}"

print(combine_names(append_with_space))
