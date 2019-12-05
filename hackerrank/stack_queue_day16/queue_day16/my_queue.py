class Queue:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return "Queue object: {}".format(self.items)

    def is_empty(self):
        """Returns a Boolean value describing whether or not the Queue is empty

        Runs in constant time.
        """
        return self.items == []

    def size(self):
        """Returns the length of the list that is representing the Queue.

        Runs in constant time because finding the length of the list also happens in constant time.
        """
        return len(self.items)

    def enqueue(self, item):
        """Takes in an item and inserts it into the 0th index of the list that is representing the Queue.

        The runtime is O(n), or linear time, because inserting into the 0th index of the list
        forces all the other items in the list to move one index to the right
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Removes and returns the front-most item of the Queue, which is represented by the last item in the list

        The runtime for this method is O(1) or constant time,
        because all it does is index to the last item of the list.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Returns the last item in the list, which is also the front-most item of the Queue

        The runtime for this method is O(1) or constant time,
        because indexing into a list is done in constant time.
        """
        if self.items:
            return self.items[-1]
        return None


if __name__ == '__main__':

    q = Queue()
    print("Queue is empty: ", q.is_empty())
    print("Queue size is 0: ", q.size() == 0)
    print("\nAdding 'apple' to the queue...")
    q.enqueue("apple")
    print("Queue is empty: ", q.is_empty())
    print("Queue size is 0: ", q.size() == 0)
    print("Queue size is {}: {}".format(q.size(), q.size() == 1))

    print("\nAdding more elements to the queue...")
    q.enqueue("banana")
    q.enqueue(43)
    q.enqueue(False)
    print("Queue size is {}: ".format(q.size()))
    print(q)

    print("Remove item from the Queue:")
    q.dequeue()
    print("Queue size is {}: ".format(q.size()))
    print(q)

    print("Get front-most item in the list: ", q.peek())
    print(q)




