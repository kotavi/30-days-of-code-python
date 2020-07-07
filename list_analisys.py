import sys

array_size = int(input("Enter the size of the list: "))
data = []
for i in range(array_size):
    num_elements = len(data)
    capacity = sys.getsizeof(data)
    print("Length: {}, size in bytes: {}".format(num_elements, capacity))

    data.append(i)

