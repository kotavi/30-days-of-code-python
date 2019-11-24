from coursera.classes.tamagotchi_game.dog import Dog



class Poodle(Dog):
    def dance(self):
        return "Dancin' in circles like poodles do."

    def hi(self):
        print(self.dance())
        super().hi()