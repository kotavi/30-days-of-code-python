
class Animal:

    def __init__(self, age):
        self.age = age
        print("An animal has been created")

    def get_age(self):
        return self.age

    def eat(self):
        print("An animal is eating")
