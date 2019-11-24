from hackerrank.abstract_class_day13.animal import Animal


class Cat(Animal):

    def __init__(self, age):
        super().__init__(age)
        print("A cat has been created")

    def meow(self):
        print("A cat says meow")

    def prance(self):
        print("A cat is prancing")

    def eat(self):
        print("A cat is eating")

    def sleep(self):
        print("A cat is sleeping")
