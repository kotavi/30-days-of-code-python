# Linked lists

See LinkedIn course https://www.linkedin.com/learning/python-data-structures-linked-lists/

Linked lists don't store their data in a continuous chunk of memory,
like Python's built-in lists do.
Instead, linked lists store their data in a series of nodes.
Each node contains the data being stored, as well as what's called a pointer.

Note: Linked lists don't contain nodes.
Instead, they have a head attribute that points to the first node of the linked list if one exists.
Otherwise, the head attribute points to None.

Operations:
1. add a node to and remove a node from the linked list.
Regardless of whether we're working with a singly linked or a doubly linked list
we need to be able to add a node to the beginning or to the end of the linked list.
2. add a node just before or just after an existing node who's data item matches something we're looking for.
This is called a key.
3. remove a node from the beginning or the end
4. remove a node that appears just before or just after a node that contains a key.
5. whether or not a linked list is empty,
6. how many nodes are in it
7. be able to find the index of a node that has a particular key.

The linked list is what's called a sequential-access data structure.
This is because we can only access a node by first accessing all the nodes that came before it.

So when does it make sense to use a linked list?
 - If you need to be able to insert items in between other items,
 - if you're working with a collection who's size is unknown,
 - if you don't need random access because again linked lists have sequential access,
and if you're not concerned about memory usage.
 - Linked lists have a unique property about them and that is that they are also recursive data structures.
 - A linked list is either empty or it's a node that contains a data item and a pointer to a linked list.
 - In this example you can see how the node on the far left is actually pointing to an entire other linked list. Likewise, the node in the middle is itself pointing to a node that then points to another linked list. We won't discuss recursion in this course, but knowing that a linked list is a recursive data structure, may come in handy in an interview. I encourage you to study more about the recursive properties of linked lists if this interests you.

