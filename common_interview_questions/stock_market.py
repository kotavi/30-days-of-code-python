"""
You will be given a list of stock prices for a given day
and your goal is to return the maximum profit that could have been made
by buying a stock at the given price and then selling the stock later on.
For example if the input is: [45, 24, 35, 31, 40, 38, 11]
then your program should return 16 because if you bought the stock at $24 and sold it at $40,
a profit of $16 was made and this is the largest profit that could be made.
If no profit could have been made, return -1.
"""

def find_max_profit_On2(inp):
    """Solved with two for loops, therefor complexity is O(n^2)"""
    n = len(inp)
    max_profit = 0

    for i in range(n - 1):
        buy = inp[i]
        for j in range(i+1, n):
            sell = inp[j]
            if sell - buy > max_profit:
                max_profit = sell - buy
    if max_profit != 0:
        return max_profit
    else:
        return  -1

print(find_max_profit_On2([45, 24, 35, 31, 40, 38, 11]))
print(find_max_profit_On2([15, 24, 35, 31, 40, 38, 11]))
print(find_max_profit_On2([15, 24, 35, 31, 40, 38, 11, 89]))

def find_max_profit_On(inp):
    """Solved with one for loop, therefor complexity is O(n)"""
    n = len(inp)
    max_profit = 0
    change_index = True
    for i in range(n - 1):
        if change_index:
            buy = inp[i]
        sell = inp[i+1]
        if sell < buy:
            change_index = True
        else:
            if sell - buy > max_profit:
                max_profit = sell - buy
                change_index = False
    return max_profit
print(find_max_profit_On([45, 24, 35, 31, 40, 38, 11]))
print(find_max_profit_On([15, 24, 35, 31, 40, 38, 11]))
print(find_max_profit_On([15, 24, 35, 31, 40, 38, 11, 89]))