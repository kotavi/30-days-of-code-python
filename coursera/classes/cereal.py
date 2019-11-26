class Cereal:

    calories = 0

    def __init__(self, name, brand, fiber):
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand,
                                                                                                self.fiber)

    def increase_calories(self):
        self.calories += 1

"""
Converting an Object to a String
"""

c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)
print(c1)
print(c2)
c2.increase_calories()
c2.increase_calories()
c2.increase_calories()
print(c2.calories)