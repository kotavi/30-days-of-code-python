from animal_day12.animal import Animal


class Dog(Animal):

    def __init__(self, age):
        Animal.__init__(self,age)
        print("A dog has been created")

    def ruff(self):
        print("A dog says ruff")

    def run(self):
        print("A dog is running")