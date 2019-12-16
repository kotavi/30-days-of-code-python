from hackerrank.stack_queue_day16.stack_day16.my_stack import Stack


class Solution:

    def add_(self, x, y):
        return x + y

    def multiply_(self, x, y):
        return x * y

    def diff_(self, x, y):
        return x - y

    def div_(self, x, y):
        return int(float(x) / float(y))

    def reverse_polish_notation(self, lst):
        switcher = {
            "+": self.add_,
            "*": self.multiply_,
            "-": self.diff_,
            "/": self.div_
        }
        stack = Stack()
        operators = "+*/-"
        for el in lst:
            if el not in operators:
                stack.push(int(el))
            else:
                if el in operators:
                    digit2 = stack.pop()
                    digit1 = stack.pop()
                    stack.push(switcher[el](digit1, digit2))
        return stack.pop()


p = ["2", "1", "+", "3", "*"]
s = Solution()
print(s.reverse_polish_notation(p))

p = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(s.reverse_polish_notation(p))
