### Trees

- hierarchical data structure;
- every item in the tree is a node;
- the node at the top of the tree is the root;
- every tree has one and only one root;
- every non-root node has one and only one parent;
- a leaf node has no children;
- every tree consists of one or more sub-trees;
- a tree with only one node in it called a ***singleton tree***.

                    (root-node)
                   /           \
          (child-node)      (child-node)
           /        \       /     |    \
        (leaf)   (leaf)  (leaf) (leaf)(leaf)

***Example of trees:***
- Java class hierarchy
- File system

*Definitions:*
<br>
**The height of the tree** is the longest path from the root to a leaf node.
<br>
**The height of a node** is the number of edges on the longest path from the node to the leaf.
<br>
**The depth of a node** is the number of edges from the node to the tree's root node.

### Binary tree

- every node has 0, 1, or 2 children;
- children are referred to as left child and right child
- a binary tree is complete if every level except the last level, has two children and on the last level, all of the nodes are as left as possible
- a full binary tree is a tree where every node other than the leaves has to have two children


### Binary search tree

- can perform insertions, deletions and retrievals in O(logn) time;
- the left child always has a smaller value than its parent;
- the right child always has a larger value than its parent;

`Insert into the tree [4,5,2,1,0,6,7,3]`

              L (4) R
                /  \
              (2)  (5)
             /  \    \
           (1) (3)   (6)
          /            \
        (0)            (7)
As a result we've got an incomplete binary tree
        
`Insert into the tree [25, 20, 15, 27, 30, 29, 26, 22, 32]`

              L (25) R
              /     \
           (20)     (27)
          /  \      /  \
       (15) (22)  (26) (30)
                       /   \
                    (29)   (32)
As a result we've got a complete binary tree

`Insert into the tree [25, 20, 17, 10]`

                (25)
                /
             (20)
             /
           (17)
           /
         (10)
As a result we've got a linked list         
