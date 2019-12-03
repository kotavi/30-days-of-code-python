from hackerrank.stack_day16.my_stack import Stack

def check_if_pairs(bracket1, bracket2):
    pairs = {"(": "", "[": "", "{": "", ")": "(", "]": "[", "}": "{"}

    return pairs[bracket1] == bracket2

def balanced_attempt1(symbols):
    n = len(symbols)
    if n % 2 != 0:
        return "Unbalanced symbols"
    s = Stack()
    s.push(symbols[0])
    print(s.items)
    i = 1
    while i < n:
        if check_if_pairs(symbols[i], s.peek()):
            s.pop()
        else:
            s.push(symbols[i])
        print(s.items)
        i += 1
    if not s.items:
        return "Balanced symbols"
    else:
        return "Unbalanced"

print(balanced_attempt1("((){[]})"))
print(balanced_attempt1("((){[{()()()}]})"))
print(balanced_attempt1("((){[{())()}])"))


def balanced_attempt2(symbols):
    n = len(symbols)
    if n % 2 != 0:
        return "Unbalanced symbols"

    pairs = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    openers = pairs.keys()
    s = Stack()
    index = 0
    while index < n:
        if symbols[index] in openers:
            s.push(symbols[index])
        else:
            if s.is_empty():
                return "Unbalanced symbols"
            else:
                if pairs[s.pop()] != symbols[index]:
                    return "Unbalanced symbols"
        index += 1
        print(s.items)

    if s.is_empty():
        return "Balanced symbols"


print(balanced_attempt2("((){[]})"))
print(balanced_attempt2("((){[{()()()}]})"))
print(balanced_attempt2("((){[{())()}])"))