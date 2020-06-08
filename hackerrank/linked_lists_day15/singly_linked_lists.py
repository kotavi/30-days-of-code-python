class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None  # when we create a new Node, it doesn't point to anything yet.

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    # methods to interact with our Node

    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute."""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next parameter."""
        self.next = new_next


if __name__ == '__main__':
    node1 = SLLNode('apple')
    print(node1.get_data())
    print(node1.get_next())
    node1.set_data(7)
    print(node1.get_data())

    # creating new node
    node2 = SLLNode('carrot')
    node1.set_next(node2)
    print(node1.get_next())