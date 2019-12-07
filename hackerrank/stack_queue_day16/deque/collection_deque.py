"""
Deques are a generalization of stacks and queues (the name is pronounced “deck”
and is short for “double-ended queue”).
Deques support thread-safe, memory efficient appends and pops from either side of the deque
with approximately the same O(1) performance in either direction.
"""

from collections import deque


def deque_operations():
    my_deque = deque()
    switcher = {
        "append": "my_deque.append(value)",
        "pop": "my_deque.pop()",
        "popleft": "my_deque.popleft()",
        "appendleft": "my_deque.appendleft(value)",
        "extend": "my_deque.extend(value)"
    }

    operations = ["append 1", "append 2", "append 3", "appendleft 4", "pop", "popleft", "extend abcw"]
    for operation in operations:
        data = operation.split()
        if len(data) == 2:
            command = data[0]
            value = data[1]
        else:
            command = data[0]
        exec(switcher[command])
    return my_deque


d = deque_operations()
for v in d:
    print(v, end=" ")
