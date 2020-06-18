def array_sum1(arr):
    n = len(arr)
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[n - 1] + array_sum1(arr[:n - 1])


def array_sum2(arr):
    if not arr:
        return 0
    else:
        return arr[0] + array_sum2(arr[1:])


print(array_sum2([1, 2, 3, 4, 5]))


def count_list(lst):
    if not lst:
        return 0
    else:
        return 1 + count_list(lst[1:])


print(count_list([1, 2, 3, 4, 5]))


def max_in_list(lst):
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = max_in_list(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


print(max_in_list([11, 4, 6, 0, 90]))
