class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "{} - {}".format(self.name, self.price)

    def sort_priority(self):
        return self.price


list_of_tuples = [("Cherry", 10), ("Apple", 5), ("Blueberry", 20), ("Raspberry",21), ("Pear", 13)]
L = []
for tup in list_of_tuples:
    L.append(Fruit(*tup))

for obj in L:
    print(obj)

print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

print("----one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)

print("----sorted by price, not referencing a class method-----")
for f in sorted(L, key=lambda x: x.price):
    print(f.name)