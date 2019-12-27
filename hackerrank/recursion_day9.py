def summation(int_number):
    # base case: the end
    if int_number <= 0:
        return 0
    # recursive case: keep going
    else:
        return int_number + summation(int_number-1)

print("\nSummation function: ")
for i in range(1, 11):
    print("0 + .. + {} = ".format(i), summation(i))


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n -1)

print("\nFactorial function: ")
for i in range(1, 11):
    print("{}! = ".format(i), factorial(i))


def exponentiation(n, exp):
    if exp == 1:
        return n
    else:
        return n * exponentiation(n, exp - 1)

print("\nExponentiation function: ")
for i in range(2, 6):
    print("{}^{} = ".format(i, 5), exponentiation(i, 5))
    # print("{}**{} = ".format(i, 5), i**5)

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    max1 = arr[0]
    max2 = find_max(arr[1:])
    if max1 > max2:
        return max1
    else:
        return max2

print("\nMax value:", find_max([12, 4, 0, -2, 45, 6]))