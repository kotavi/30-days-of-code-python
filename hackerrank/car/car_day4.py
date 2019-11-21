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

    def get_max_speed(self):
        return self.max_speed

    def set_max_speed(self, new_max_speed):
        self.max_speed = new_max_speed

    def get_condition(self):
        return self.condition

    def set_condition(self, new_condition):
        self.condition = new_condition

    def get_car_name(self):
        return self.name_of_car

    def set_car_name(self, new_name):
        self.name_of_car = new_name


    def upgrade_max_speed(self):
        return self.set_max_speed(self.get_max_speed() + 10)

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
family_car.set_condition('D')
family_car.set_car_name("New Cool Name")
family_car.upgrade_max_speed()
print("\nFamily's car:")
family_car.print_params()


print("Miles left: ", family_car.how_many_miles_till_out_of_gas())
print("Max miles: ", family_car.max_miles_per_fill_up())

