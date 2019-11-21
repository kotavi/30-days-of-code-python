import random
import json
import os


def print_instructions():
    print("Welcome to the Mad Libs game. "
          "If you type in words, we'll give you a story. "
          "Start by typing in a name: ")

def retrieve_words():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'words.json')) as file:
        words = json.load(file)
    return words['nouns'], words['adjectives'], words['adverbs']

nouns, adjectives, adverbs = retrieve_words()


class MadLibs:

    def __init__(self):
        self.name = ""
        self.story = ""
        self.adjective1 = ""
        self.adjective2 = ""
        self.noun1 = ""
        self.noun2 = ""
        self.noun3 = ""
        self.adverb = ""
        self.random_numbers = ""

    # Getters and setters

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_story(self):
        return self.story

    def set_story(self, new_story):
        self.story = new_story

    def get_adjective1(self):
        return self.adjective1

    def set_adjective1(self, new_adjective1):
        self.adjective1 = new_adjective1

    def get_adjective2(self):
        return self.adjective2

    def set_adjective2(self, new_adjective2):
        self.adjective2 = new_adjective2

    def get_noun1(self):
        return self.noun1

    def set_noun1(self, new_noun1):
        self.noun1 = new_noun1

    def get_noun2(self):
        return self.noun2

    def set_noun2(self, new_noun2):
        self.noun2 = new_noun2

    def get_noun3(self):
        return self.noun3

    def set_noun3(self, new_noun3):
        self.noun3 = new_noun3

    def get_adverb(self):
        return self.adverb

    def set_adverb(self, new_adverb):
        self.adverb = new_adverb

    def get_random_numbers(self):
        return self.random_numbers

    def set_random_numbers(self):
        num = random.randrange(1,10)
        index = 0
        number_holder = []
        while index < 3:
            number_holder.append(num + index)
            index += 1
        self.random_numbers = "not {}, not {}, but {}".format(number_holder[0], number_holder[1], number_holder[2])

    def enter_name(self):
        self.set_name(input())

    def enter_nouns(self):
        users_nouns = input("Give me three nouns (separated by coma): ").split(',')
        for noun in users_nouns:
            if noun not in nouns:
                print("Make sure you are entering a correct noun!")
        self.set_noun1(users_nouns[0])
        self.set_noun2(users_nouns[1])
        self.set_noun3(users_nouns[2])

    def enter_adjectives(self):
        users_adjectives = input("Give me two adjectives (separated by coma): ").split(',')
        for adjective in users_adjectives:
            if adjective not in adjectives:
                print("Make sure you are entering a correct adjective!")
        self.set_adjective1(users_adjectives[0])
        self.set_adjective2(users_adjectives[1])

    def enter_adverb(self):
        adverb = input("Give me one adverb: ")
        if adverb not in adverbs:
            print("Make sure you are entering a correct adjective!")
        self.set_adverb(adverb)

    def put_together_a_story(self):
        number = random.random()
        if number == 0:
            story = "Jessy and her best friend " + self.get_name() + " went to Disney World today!" + \
                    "They saw a " + self.get_noun1() + " in a show at the Magic Kingdom " + \
                    "and ate a " + self.get_adjective1() + " feast for dinner. The next day I " + \
                    "ran " + self.get_adverb() + " to meet Mickey Mouse in his " + self.get_noun2() + \
                    " and then that night I gazed at the " + self.get_random_numbers() + \
                    " " + self.get_adjective2() + " fireworks shooting from the " + self.get_noun3() + "."
        else:
            story = "Amanda and her frenemy " + self.get_name() + " went to the zoo last summer. " + \
                    "They saw a huge " + self.get_noun1() + " and a tiny little " + self.get_noun2() + \
                    ". That night they decided to climb " + self.get_adverb() + " in to the " + self.get_noun3() + \
                    " to get a closer look. The zoo was " + self.get_adjective1() + " at night, but they didn't care " + \
                    "... until " + self.get_random_numbers() + " " + self.get_adjective2() + " apes yelled in their faces, " + \
                    "making Amanda and " + self.get_name() + " sprint all the way back home."
        self.set_story(story)

    def play(self):
        self.enter_name()
        self.enter_nouns()
        self.enter_adjectives()
        self.enter_adverb()
        self.set_random_numbers()
        self.put_together_a_story()
        print(self.get_story())


game = MadLibs()
print_instructions()
game.play()

