import random
from coursera.final_exams.wheel_of_fortune.player import WOFPlayer

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
VOWEL_COST = 250

class WOFComputerPlayer(WOFPlayer):

    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smart_coin_flip(self):
        rnd_num = random.randint(1, 11)
        print("rnd_num: ", rnd_num)
        if rnd_num > self.difficulty:
            return True
        else:
            return False

    def get_possible_letters(self, guessed):
        letters_without_guessed = [letter for letter in LETTERS if letter not in guessed]
        if self.prize_money >= 250:
            return letters_without_guessed
        return [letter for letter in letters_without_guessed if letter not in VOWELS]

    def get_move(self, category, obscurePhrase, guessed):
        possible_letters = self.get_possible_letters(guessed)
        print(possible_letters)
        if not possible_letters:
            return "pass"
        letters = [l for l in self.SORTED_FREQUENCIES if l not in guessed]
        print(letters)
        if self.prize_money >= 250:
            if self.smart_coin_flip():
                return letters[-1]
            else:
                return random.choice(letters)
        else:
            no_vowels = [l for l in letters if l not in VOWELS]
            print(no_vowels)
            if self.smart_coin_flip():
                return no_vowels[-1]
            else:
                return random.choice(no_vowels)
