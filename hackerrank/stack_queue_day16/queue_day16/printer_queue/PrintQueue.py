class PrintQueue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return "Queue object: {}".format(self.items)

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None
