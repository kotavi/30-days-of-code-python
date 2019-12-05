from abc import ABCMeta, abstractmethod


class AdvancedArithmetic(object, metaclass=ABCMeta):
    @abstractmethod
    def divisor_sum(self, value): pass


class Calculator(AdvancedArithmetic):
    def divisor_sum(self, value):
        sum_res = 0
        for i in range(1, value + 1):
            if n % i == 0:
                sum_res += i
        return sum_res


if __name__ == '__main__':
    n = int(input())
    my_calculator = Calculator()
    s = my_calculator.divisor_sum(n)
    print("I implemented: " + type(my_calculator).__bases__[0].__name__)
    print(s)
