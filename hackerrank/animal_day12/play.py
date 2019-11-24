from hackerrank.animal_day12.animal import Animal
from hackerrank.animal_day12.cat import Cat
from hackerrank.animal_day12.dog import Dog

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