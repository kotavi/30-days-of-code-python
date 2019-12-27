### Trees

- hierarchical data structure;
- every item in the tree is a node;
- the node at the top of the tree is the root;
- every tree has one and only one root;
- every non-root node has one and only one parent;
- a leaf node has no children;
- a tree with only one node in it called a singleton tree.

                    (root-node)
                   /           \
          (child-node)      (child-node)
           /        \       /     |    \
        (leaf)   (leaf)  (leaf) (leaf)(leaf)


*Definitions:*
<br>
**The height of the tree** is the longest path from the root to a leaf node.
<br>
**The depth of a node** is the number of edges from the node to the tree's root node.

### Binary tree

- every node has 0, 1, or 2 children;
- children are referred to as left child and right child



### Binary search tree

- can perform insertions, deletions and retrievals in O(logn) time;
- the left child always has a smaller value than its parent;
- the right child always has a larger value than its parent;
- everything to left of the root or to the left of a parent is less than the value of the root or the parent and everything to the right of the root or the parent is greater than the value of the root or the parent



[4,5,2,1,0,6,7,3]

      L (4) R
        / \
     (2)  (5)
    /  \  /  \
   ()