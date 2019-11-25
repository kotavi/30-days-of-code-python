a1 = [5, 6, 7]

a2 = ['a', 'b', 'c']

print(zip(a2, a1))
dict_zip = dict(zip(a2, a1))
print(dict_zip)
list_zip = list(zip(a2, a1))
print(list_zip)

for x1, x2 in list_zip:
    print("{}".format(x2*x1))


a3 = [4, 5, 6]
list_zip = list(zip(a1, a3))
for x1, x2 in list_zip:
    print("{}".format(x2 + x1))

list_compr = [x2 + x1 for (x2, x1) in list(zip(a1, a3))]
print(list_compr)

map_zip = map(lambda x: x[0] + x[1], zip(a1, a3))
print(list(map_zip))


print("""Write code using zip and filter so that these lists (l1 and l2) are combined into one big list 
and assigned to the variable opposites if they are both longer than 3 characters each.""")
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
tuples = list(zip(l1, l2))
opposites = list(filter(lambda w: len(w[0]) > 3 and len(w[1]) > 3, zip(l1, l2)))
print(opposites)

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print(X)
print(list(zip(*X)))


def avg_marks():
    """
    5 3
    89 90 78 93 80
    90 91 85 88 86
    91 92 83 89 90.5
    """
    # n - number of students
    # x - number of subjects
    n, x = map(int, input().split())
    marks = []
    for i in range(x):
        marks.append(list(map(float, input().split())))

    for tup in list(zip(*marks)):
        print(sum(tup) / len(tup))

