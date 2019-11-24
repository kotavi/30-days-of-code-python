from coursera.classes.tamagotchi_game.pet import Pet

from random import randrange


class Bird(Pet):
    sounds = ["chirp"]

    def __init__(self, name="Kitty", chirp_number=2):
        super().__init__(name)  # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
        self.chirp_number = chirp_number  # now, also assign the new instance variable

    def hi(self):
        for i in range(self.chirp_number):
            print(i)
            print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

if __name__ == '__main__':
    b1 = Bird('tweety', 5)
    b1.teach("Polly wanna cracker")
    b1.hi()

    print(b1.sounds) # The interpreter finds the value in the class variable for the class Bird.
