from hackerrank.abstract_class_day13.animal import Animal


class Dog(Animal):

    def __init__(self, age):
        super().__init__(age)
        print("A dog has been created")

    def ruff(self):
        print("A dog says ruff")

    def run(self):
        print("A dog is running")

    def eat(self):
        print("A dog is eating")

    def sleep(self):
        print("A dog is sleeping")
