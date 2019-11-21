
class Animal:

    def __init__(self, age):
        self.age = age
        print("An animal has been created")

    def get_age(self):
        return self.age

    def eat(self):
        print("An animal is eating")


class Cat(Animal):

    def __init__(self, age):
        super().__init__(age)
        print("A cat has been created")

    def meow(self):
        print("A cat says meow")

    def prance(self):
        print("A cat is prancing")


class Dog(Animal):

    def __init__(self, age):
        super().__init__(age)
        print("A dog has been created")

    def ruff(self):
        print("A dog says ruff")

    def run(self):
        print("A dog is running")

if __name__ == '__main__':

    animal = Animal(8)
    dog = Dog(3)
    cat = Cat(4)

    dog.ruff()
    cat.meow()

    dog.eat()
    cat.eat()

    dog.run()
    cat.prance()

    print(dog.get_age())
    print(dog.age)
    print(cat.get_age())
    print(cat.age)

