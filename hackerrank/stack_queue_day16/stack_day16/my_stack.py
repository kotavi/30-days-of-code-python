class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this method is O(1) or constant time,
        because appending to the end of the list happens in constant time.
        """

        self.items.append(item)

    def pop(self):
        """Removes and returns the last item for the list, which is also the top item of the Stack

        The runtime for this method is O(1) or constant time,
        because all it does is index to the last item of the list.
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """Returns the last item in the list, which is also the top item of the Stack

        The runtime for this method is O(1) or constant time,
        because indexing into a list is done in constant time.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the length of the list that is representing the Stack.

        Runs in constant time because finding the length of the list also happens in constant time.
        """
        return len(self.items)

    def is_empty(self):
        """Returns a Boolean value describing whether or not the Stack is empty

        Runs in constant time.
        """
        return self.items == []


if __name__ == '__main__':

    stack = Stack()
    print("Push:")
    stack.push("apple")
    print(stack.items)
    stack.push("banana")
    stack.push("carrot")
    print(stack.items)

    print("Pop:")
    stack.pop()
    print(stack.items)
    stack.pop()
    print(stack.items)
    stack.pop()
    print(stack.items)

    print("Peek: ")
    stack.push("apple")
    stack.push("banana")
    stack.push("carrot")
    print(stack.items)
    print(stack.peek())

    print("Size: ")
    print(stack.size())

