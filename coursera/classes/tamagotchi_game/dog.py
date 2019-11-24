from coursera.classes.tamagotchi_game.pet import Pet


class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def feed(self):
        """
        since we are not invoking the method the normal way, with <obj>.methodname,
        we have to explicitly pass an instance as the first parameter.
        In this case, the variable self in Dog.feed() will be bound to an instance of Dog,
        and so we can just pass self: Pet.feed(self).
        """
        Pet.feed(self)
        print("Arf! Thanks!")

    def teach(self, word):
        """
        super().teach(word): it easier to read,
        it puts the specification of the class that Dog inherits from in just one place, class Dog(Pet).
        You just refer to super() and python takes care of looking up that the parent (super) class of Dog is Pet.
        """
        super().teach(word)
        print("Arf! Thanks for teaching me a new word!")

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"

if __name__ == '__main__':
    d1 = Dog("Astro")
    print(d1)
    d1.feed()
    print(d1)
    for i in range(6):
        d1.clock_tick()
    print(d1)
    d1.hi()
    d1.teach("Gafff")

