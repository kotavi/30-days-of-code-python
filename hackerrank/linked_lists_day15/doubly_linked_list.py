class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None # when we create a new Node, it doesn't point to anything yet.
        self.previous = None

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

    def get_previous(self):
        """Return the self.previous attribute."""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value of the self.previous attribute with new_previous parameter."""
        self.previous = new_previous

if __name__ == '__main__':

    node1 = DLLNode('apple')
    node2 = DLLNode('carrot')
    node1.set_next(node2)
    node3 = DLLNode(34)
    node2.set_next(node3)
    node2.set_previous(node1)
    node3.set_previous(node2)

    print("Node1.\nNext: {}, Previous: {}".format(node1.get_next(), node1.get_previous()))
    print("Node2.\nNext: {}, Previous: {}".format(node2.get_next(), node2.get_previous()))
    print("Node3.\nNext: {}, Previous: {}".format(node3.get_next(), node3.get_previous()))