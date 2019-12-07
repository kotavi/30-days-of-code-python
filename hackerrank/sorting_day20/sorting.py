arr = [2, 4, 0, -1, 3]
n = len(arr)

# Bubble sort
for i in range(n):
    # Track number of elements swapped during a single array traversal
    numberOfSwaps = 0
    for j in range(n - 1):
        # Swap adjacent elements if they are in decreasing order
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
    numberOfSwaps += 1

print(arr)