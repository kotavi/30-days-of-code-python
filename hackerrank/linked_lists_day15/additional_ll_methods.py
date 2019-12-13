from hackerrank.linked_lists_day15.singly_linked_lists import SLLNode
from hackerrank.linked_lists_day15.sll import SLL

if __name__ == '__main__':

    # Linked List
    print("LinkedList1: ")
    sll = SLL()
    print("LinkedList1 is empty: ", sll.is_empty())
    node = SLLNode(5)
    sll.head = node
    sll.display_linked_list()
    print("\nCreating a linked list with a loop")
    sll.add_end(6)
    sll.add_end(8)
    sll.add_end(11)
    node = SLLNode(23)
    last_node = sll.return_last_node()
    last_node.next = node
    mid_node = sll.find_middle()
    node.set_next(mid_node)
    print("Loop: head --> 5 --> 6 --> 8 --> 11 --> 23 --> 8 --> 11 --> 23 --> ... --> 8 --> 11 --> 23 --> ...")

    print("Loop exists: ", sll.detect_loop)
    print("\nLinkedList2: ")
    sll2 = SLL()
    sll2.add_end(3)
    sll2.add_end(5)
    sll2.add_end(8)
    sll2.display_linked_list()
    print("\nLoop exists: ", sll2.detect_loop)


