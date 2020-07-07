# 10
# 1*1 + 0*0 = 1
# 13
# 1 * 1 + 3 *3 = 10
# -> .. -> 1*1 + 0*0 = 1
# 123 -> 1 * 1 + 2 * 2 + 3 * 3 -> 14 -> 1 * 1 + 4* 4 -> 17 -> ....


def get_sum_of_sq(num):
    lst = []
    while num > 0:
        lst.append(num % 10)
        num = num // 10
    return sum([x*x for x in lst])


temp = []


def define_if_happy(num):
    print(temp)
    if num == 1:
        return True
    if num not in temp:
        temp.append(num)
    else:
        return False
    if define_if_happy(get_sum_of_sq(num)):
        return True
    return False


def define_if_happy_2(num):
    my_set = set()
    while num not in my_set:
        my_set.add(num)
        num = get_sum_of_sq(num)
        if num == 1:
            return True
    return False

#10 -> define_if_happy(get_sum_of_sq(10), [10]])
#10 -> define_if_happy(1, [10]])

print(define_if_happy_2(123))
temp = []
print(define_if_happy_2(10))
temp = []
print(define_if_happy_2(13))
