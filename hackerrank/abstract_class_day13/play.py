from hackerrank.abstract_class_day13.cat import Cat
from hackerrank.abstract_class_day13.dog import Dog

if __name__ == '__main__':

    dog = Dog(3)
    cat = Cat(4)

    dog.ruff()
    cat.meow()

    dog.eat()
    cat.eat()

    dog.run()
    cat.prance()

    cat.sleep()
    dog.sleep()