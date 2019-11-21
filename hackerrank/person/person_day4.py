class Person:

    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def am_i_old(self):
        if self.get_age() < 0:
            print("Age is not valid, setting age to 0.")
            self.set_age(0)
        if self.get_age() < 13:
            print("You are young.")
        elif 13 <= self.get_age() < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def year_passes(self):
        return self.set_age(self.get_age() + 1)

t = int(input("Please enter a number of tries: "))
for i in range(0, t):
    age = int(input("Please enter the age: "))
    p = Person(age)
    p.am_i_old()
    for j in range(0, 3):
        p.year_passes()
    print("")