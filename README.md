# BinaryTree
Object-oriented binary tree simulation with traversal, search and delete functions

### HOW TO USE CODE + EXAMPLE

- To initialise a tree, simply create a Tree object and pass in the numerical value of the 
root node
- To add a node, call the addNode() function and pass in the numerical value of the new node, as well as the
 index of the parent node in the tree list.
- To delete a node, run the delNode() function and pass in the numerical value of the node
- To search for a node, run the searchNode() function and pass in the numerical value of the node
- To run a traversal, run the runTraversal() function and pass in either 'preOrder', 'inOrder' or 'postOrder'.

Below is example code for a binary tree, which can be found here: https://imgur.com/h1oytYV


`tree = Tree(47)`

`tree.addNode(21, 0)`

`tree.addNode(52, 0)`

`tree.addNode(11, 1)`

`tree.addNode(28, 1)`

`tree.addNode(25, 4)`

`tree.addNode(33, 4)`

`tree.addNode(30, 6)`

`tree.addNode(41, 6)`

`tree.addNode(51, 2)`

`tree.addNode(66, 2)`

`tree.runTraversal('postOrder')`
