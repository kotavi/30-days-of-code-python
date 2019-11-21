import array


def print_array():
    a = array.array("B", range(16))  # unsigned char
    b = array.array("h", range(16))  # signed short

    print(a)
    print(repr(a.tolist()))

    print(b)
    print(repr(b.tobytes()))


class ArrayPractice:

    int_array1 = array.array("i")
    int_array2 = array.array("i", range(4))
    int_array3 = array.array("i", [5, 2, 9, 1, 3])
    # shopping_list = array.array(["bananas", "apples", "pears"])

    def test(self):
        print(self.int_array2.tolist())
        print(self.int_array3.tolist())

    def __init__(self):
        pass

print_array()

arr = ArrayPractice()
arr.test()