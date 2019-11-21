import random

class CoinToss:

    def __init__(self):
        pass

    def toss_a_coin(self):
        toss = random.randint(0, 1)
        if toss == 1:
            return "HEADS"
        else:
            return "TAILS"

my_coin = CoinToss()

for i in range(10):
    print(my_coin.toss_a_coin())
