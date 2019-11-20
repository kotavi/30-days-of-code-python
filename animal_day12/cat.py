from animal_day12.animal import Animal


class Cat(Animal):

    def __init__(self, age):
        Animal.__init__(self, age)
        print("A cat has been created")

    def meow(self):
        print("A cat says meow")

    def prance(self):
        print("A cat is prancing")