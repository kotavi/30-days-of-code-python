"""
https://leetcode.com/problems/lemonade-change/
"""


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def lemonade_change(bills):
    stack = Stack()

    for bill in bills:
        if bill == 5:
            stack.push(5)
        else:
            if stack.is_empty():
                return False
            stack.push(5)
            num_of_fives = bill // 5
            if stack.size() >= num_of_fives:
                for i in range(num_of_fives):
                    stack.pop()
    return True


print(lemonade_change([5,5,5,10,20, 5, 50]))
print(lemonade_change([5, 5, 5, 10, 20]))
print(lemonade_change([5, 5, 10]))
print(lemonade_change([10, 10]))
print(lemonade_change([5, 5, 10, 10, 20]))


