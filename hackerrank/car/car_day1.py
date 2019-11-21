class Car:

    def __init__(self):
        # instance variables
        self.max_speed = 100
        self.min_speed = 0
        self.weight = 4097
        self.is_the_car_on = False
        self.condition = 'A'
        self.name_of_car = "Lucy"

    # methods

    def print_params(self):
        print(self.max_speed)
        print(self.min_speed)
        print(self.weight)
        print(self.is_the_car_on)
        print(self.condition)
        print(self.name_of_car)

    def wreck_car(self):
        self.condition = 'C'


family_car = Car()
print("Family's car:")
family_car.print_params()

my_car = family_car

family_car.wreck_car()
print("My car:")
my_car.print_params()
