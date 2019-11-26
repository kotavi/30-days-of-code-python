from coursera.final_exams.wheel_of_fortune.player import WOFPlayer

class WOFHumanPlayer(WOFPlayer):

    def get_move(self, category, obscured_phrase, guessed):
        print("{} has ${}\n\nCategory: {}\nPhrase:  {}\nGuessed: {}".format(self.name, self.prize_money, category,
                                                                            obscured_phrase, guessed))
        print("\n\nGuess a letter, phrase, or type 'exit' or 'pass':")
        move = input("Enter your move: ")
        return move