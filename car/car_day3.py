class Car:

    def __init__(self, max_speed, min_speed, weight, is_the_car_on, condition, name_of_car,
                 max_fuel, current_fuel, mpg, number_of_ppl_in_car):
        # instance variables
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.weight = weight
        self.is_the_car_on = is_the_car_on
        self.condition = condition
        self.name_of_car = name_of_car

        self.max_fuel = max_fuel
        self.current_fuel = current_fuel
        self.mpg = mpg
        self.number_of_ppl_in_car = number_of_ppl_in_car
        self.max_number_of_ppl_in_car = 6

    # methods

    def print_params(self):
        print("-----------------------------")
        print(self.max_speed)
        print(self.min_speed)
        print(self.weight)
        print(self.is_the_car_on)
        print(self.condition)
        print(self.name_of_car)
        print(self.max_fuel)
        print(self.current_fuel)
        print(self.mpg)
        print(self.number_of_ppl_in_car)

    def wreck_car(self):
        self.condition = 'C'

    def get_in(self):
        if self.number_of_ppl_in_car < self.max_number_of_ppl_in_car:
            self.number_of_ppl_in_car += 1
            print("One person got in")
        else:
            print("There are already %s people in the car" % self.max_number_of_ppl_in_car)

    def get_out(self):
        if self.number_of_ppl_in_car > 0:
            self.number_of_ppl_in_car -= 1
            print("One person got out")
        else:
            print("There are no people in the car")

    def how_many_miles_till_out_of_gas(self):
        return self.current_fuel * self.mpg

    def max_miles_per_fill_up(self):
        return self.max_fuel * self.mpg

    def turn_car_on(self):
        if not self.is_the_car_on:
            self.is_the_car_on = True
        else:
            print("The car is already on: %s" % self.is_the_car_on)

family_car = Car(100, 0, 4097, False, 'A', 'Lucy', 12, 6, 23, 2)
print("\nFamily's car:")
family_car.print_params()

my_car = family_car

family_car.wreck_car()
print("\nMy car:")
my_car.get_in()
my_car.get_in()
my_car.get_in()
my_car.get_in()
my_car.get_in()
my_car.get_out()
my_car.get_in()
my_car.get_out()
my_car.get_out()
my_car.get_out()

my_car.print_params()

print("Miles left: ", my_car.how_many_miles_till_out_of_gas())
print("Max miles: ", my_car.max_miles_per_fill_up())

my_car.turn_car_on()
my_car.turn_car_on()

my_car.print_params()

print("mpg: ", my_car.mpg)

