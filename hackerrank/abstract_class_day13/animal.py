from abc import ABC, abstractmethod
class Animal(ABC):

    def __init__(self, age):
        self.age = age
        print("An animal has been created")

    def get_age(self):
        return self.age

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass