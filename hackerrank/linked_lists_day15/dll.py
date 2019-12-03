# A doubly Linked List data structure.
from hackerrank.linked_lists_day15.doubly_linked_list import DLLNode


class DLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        return "<DLL object: head={}>".format(self.head)

    def is_empty(self):
        return self.head is None

    def search(self, data):
        """Traverses the Linked List and returns true if the data searched for is present in one of the nodes.
        Otherwise, it returns false.

        The time complexity is O(n): in the worst case we have to go through every Node of the Linked List
        to find what we are looking for.
        """
        if self.head is None:
            return False
        current = self.head
        while current:
            if current.get_data() == data:
                return True
            current = current.get_next()
        return False

    def add_front(self, data):
        """Add a Node whose data is the new_data argument to the front of the
        Linked List."""
        new_node = DLLNode(data)
        new_node.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(new_node)
        self.head = new_node
        self.size += 1

    def remove(self, data):
        """Removes the first occurrence of a Node that contains the data argument
        as its self.data attribute. Returns nothing.

        The time complexity is O(n) because in the worst case, we have to visit
        every Node before finding the one we want to remove.
        """
        if self.head is None:
            return "The Linked List is empty, nothing to remove."
        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "Data doesn't exist in the Linked List, nothing to remove."
                else:
                    current = current.get_next()
        # if we are at the first and last Node
        if current.previous is None and current.next is None:
            self.head = current.get_next()
        # if we are at the first but not last Node
        elif current.previous is None:
            # node_to_remove = self.head
            self.head.next.set_previous(None)
            self.head = self.head.get_next()
            self.head.set_next(None)
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())
        self.size -= 1

if __name__ == '__main__':
    dll = DLL()
    print(dll, "/ Linked list is empty: ", dll.is_empty())
    dll.add_front("apple")
    print(dll, "/ Linked list is empty: ", dll.is_empty())
    print("The size of the Linked List: ", dll.size)
    print("\n Adding data to the front:")
    dll.add_front("red apple")
    dll.add_front("mellon")
    print(dll, "/ The size of the Linked List: ", dll.size)

    print("\nSearch for data:")
    print("'apple' is in the list: ", dll.search('apple'))
    print("'green apple' is in the list: ", dll.search('green apple'))

    print("\nCreating a new Doubly Linked List")
    dll2 = DLL()
    print("Added data to the front")
    dll2.add_front("45")
    print("The new node's previous and next attributes are still defaulting to None")
    print(dll2.head.previous)
    print(dll2.head.next)
    print("Added data to the front")
    dll2.add_front("450F")
    print("Head: ", dll2.head)
    print("Previous: ", dll2.head.previous)
    print("Next: ", dll2.head.next)
    print("Next Previous: ", dll2.head.next.previous)
    print("Next Next: ", dll2.head.next.next)
    print("Size: ", dll2.size)

    print("\nRemoving data:")
    print("- when data doesn't exist: ", dll2.remove("apple"))
    print("- when data is in 1st Node: ", dll2.remove("450F"))
    print("Head: ", dll2.head)
    print("Previous: ", dll2.head.previous)
    print("Next: ", dll2.head.next)
    print("Size: ", dll2.size)

    print("- when data is in 1st Node: ", dll2.remove("45"))
    print(dll2)
    print(dll2.head)
    print("Size: ", dll2.size)
