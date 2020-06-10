class Stack:

    def __init__(self):
        self.items = []
        self.min = None

    def push(self, item):
        if not self.items:
            self.min = item
        else:
            if item < self.min:
                self.min = item
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push(0)
    stack.push(-1)
    stack.push(8)
    stack.push(5)
    print("Stack items: ", stack.items)
    print("Stack min  :", stack.min)

