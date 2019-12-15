# A singly Linked List data structure.
from hackerrank.linked_lists_day15.singly_linked_lists import SLLNode


class SLL:
    def __init__(self):
        self.head = None  # when we first create a new singly Linked List object, we haven't yet associated any nodes to it.

    def __repr__(self):
        return "SLL object: head={}".format(self.head)

    def is_empty(self):
        """Returns True if Linked List is empty. Otherwise, returns False"""
        return self.head is None

    def add_front(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the Linked List"""
        new_node = SLLNode(new_data)
        new_node.set_next(self.head)
        self.head = new_node

    def add_end(self, new_data):
        """Add a Node whose data is the new_data argument to the end of the Linked List"""
        new_node = SLLNode(new_data)
        if self.head is None:
            self.head = new_node
            return self.head
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        return self.head

    def size(self):
        """Traverses the Linked List and returns an integer value representing the number of nodes in the Linked List.

        The time complexity is O(n): every Node of the Linked List must be visited in order to calculate
        the size of the Linked List
        """
        current = self.head
        result = 0
        if self.head is None:
            return 0
        while current:
            result += 1
            current = current.get_next()
        return result

    def search(self, data):
        """Traverses the Linked List and returns true if the data searched for is present in one of the nodes.
        Otherwise, it returns false.

        The time complexity is O(n): in the worst case we have to go through every Node of the Linked List
        to find what we are looking for.
        """
        if self.head is None:
            return "Linked List is empty. No Nodes to search"
        current = self.head
        while current:
            if current.get_data() == data:
                return True
            current = current.get_next()
        return False

    def display_linked_list(self):
        if self.head is None:
            return self.head
        current = self.head
        while current:
            print(current.get_data(), end=" --> ")
            current = current.get_next()

    def remove(self, data):
        """Remove Node from Linked List"""
        # Case 1. Linked List is empty
        if self.head is None:
            return "There are no Nodes to remove"

        # Case 2. The data is not in the Linked List
        if not self.search(data):
            return "Data doesn't exist in the Linked List"

        current = self.head
        # Case 3. It's a first node to remove
        if current.get_data() == data:
            self.head = current.get_next()
            current.set_next(None)
            return

        prev = None
        found = False
        while not found:
            # Case 4. When the data is elsewhere in the Linked List
            if current.get_data() != data:
                prev = current
                current = current.get_next()
            else:
                found = True
                prev.next = current.next
                current.set_next(None)

    def remove_node(self, data):
        """Deletes a node (except the tail) in a singly linked list.
            - The linked list will have at least two elements.
            - All of the nodes' values will be unique.
            - The given node will not be the tail and it will always be a valid node of the linked list.
        """
        current = self.head
        if current.get_data() == data:
            self.head = current.next
            current.set_next(None)
            return
        while current.next:
            if current.next.data == data:
                node_to_remove = current.next
                current.set_next(node_to_remove.next)
                node_to_remove.set_next(None)
            current = current.next



    def return_last_node(self):
        """Returns the last Node of the Linked List"""
        last = self.head
        if self.head is None:
            return None
        while last.next:
            last = last.get_next()
        return last

    def find_middle(self):
        mid = self.size()//2
        current = self.head
        for i in range(mid):
            current = current.next
        return current

    @property
    def detect_loop(self):
        ht = set()
        current = self.head
        while current:
            if current in ht:
                return "True"
            else:
                ht.add(current)
            current = current.next
        return "False"



if __name__ == '__main__':

    # Linked List
    print("LinkedList1: ")
    sll = SLL()
    print("LinkedList1 is empty: ", sll.is_empty())
    node = SLLNode(5)
    sll.head = node
    print("Added a new Node to the list, LinkedList1 is empty: ", sll.is_empty())
    sll.add_end("banana")
    print("Added a new Node to the end, LinkedList1 size is: ", sll.size())
    sll.add_front("apple")
    print("Added a new Node to the front, LinkedList1 size is: ", sll.size())
    print("LinkedList1 is: ")
    sll.display_linked_list()

    print("\n\nLinkedList2: ")
    sll2 = SLL()
    my_lst = [2, 3, 4, 1]
    print("Adding data to the front in the for loop:")
    for value in my_lst:
        sll2.add_front(value)
        print("head: {}".format(sll2.head))
    sll2.display_linked_list()
    print("\nHead points to the last added element {}: {}".format(my_lst[-1], sll2.head))
    print("Size after we added {} to the Linked List: {}".format(my_lst, sll2.size()))

    print("\nLinkedList3: ")
    sll3 = SLL()
    print("Size when there is no elements in the Linked List: ", sll3.size())
    print("Add new Node to the end of the Linked List")
    sll3.add_end("banana3")
    print("New size: ", sll3.size())
    sll3.add_end(12.45)
    sll3.add_end(["hello"])
    sll3.display_linked_list()
    print("\nHead is on: ", sll3.head)

    print("\nSearching for data")
    print(sll2.search(4))  # True
    print(sll2.search(8))  # False
    print(sll3.search(8))  # Linked List is empty. No Nodes to search

    print("\nRemoving data from Linked List")
    print("LinkedList3: ")
    sll3.add_end(34)
    sll3.add_end("Welcome")
    sll3.add_end("a")
    sll3.add_end("b")
    sll3.add_end("c")
    print(sll3.display_linked_list())
    print("When data 'apple' does not exist: ")
    print(sll3.remove("apple"))
    print("When data is the 1st element in the Linked List: ")
    sll3.remove("banana3")
    print(sll3.display_linked_list())
    print("When data is elsewhere in the Linked List: ")
    sll3.remove("Welcome")
    print(sll3.display_linked_list())
    print("Find middle node in the Linked List: ")
    print(sll3.find_middle())

