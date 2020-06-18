"""
https://leetcode.com/problems/lemonade-change/
"""


def lemonade_change(bills):
    five = ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if not five:
                return False
            five -= 1
            ten += 1
        else:
            if five and ten:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True


print(lemonade_change([5, 5, 5, 10, 20, 5]))
print(lemonade_change([5, 5, 5, 10, 20]))
print(lemonade_change([5, 5, 10]))
print(lemonade_change([10, 10]))
print(lemonade_change([5, 5, 10, 10, 20]))

1010
