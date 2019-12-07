class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def peek_rear(self):
        if self.items:
            return self.items[-1]
        return None

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None

if __name__ == '__main__':

    d = Deque()
    d.add_rear("apple")
    d.add_rear("red apple")
    d.add_rear("banana")
    d.add_front("carrot")
    d.add_front("pear")

    print(d.items)
    print(d.size())

    print("Item to be removed: {}".format(d.peek_front()))
    d.remove_front()
    print(d.items)
    print("Item to be removed: {}".format(d.peek_rear()))
    d.remove_rear()
    print(d.items)
    print(d.size())