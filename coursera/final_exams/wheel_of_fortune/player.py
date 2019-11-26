class WOFPlayer:
    prize_money = 0  # The amount of prize money for this player
    prizes = []  # The prizes this player has won so far

    def __init__(self, name):
        self.name = name  # The name of the player
        self.prizes = self.prizes[:]

    def add_money(self, amt):
        self.prize_money += amt

    def go_bankrupt(self):
        self.prize_money = 0

    def add_prize(self, prize):
        self.prizes.append(prize)
        print("self.prizes: ", self.prizes)
        print("self: ", self)

    def __str__(self):
        return "{} (${})".format(self.name, self.prize_money)