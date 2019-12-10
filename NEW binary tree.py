"""
The Node class represents each different node on a tree. Each node has:
- value: The integer value of the node
- parent: The list index of the parent node in Tree.tree
- children: A set-length list, where children[0] is the left child and children[1] is the right child
- treeIdx: The list index of the node in Tree.tree
"""

class Node():
    def __init__(self, value, parent, treeIdx):
        self.value = value
        self.parent = parent
        self.children = [None, None]
        self.treeIdx = treeIdx

    def addChild(self, childValue, childIdx): #Sets child as either left/right depending on childValue
        if childValue < self.value:
            self.children[0] = childIdx
        else:
            self.children[1] = childIdx

    def killChild(self, childIdx): #Removes child by index (0 or 1)
        for child in range(len(self.children)):
            if self.children[child] == childIdx:
                self.children[child] = None

    def setParent(self, parentIdx):
        self.parent = parentIdx

"""
The Tree class tracks each Node object and allows for searching, deletion, and traversal of the binary tree.
- tree: Unordered list that stores each node
"""

class Tree():
    def __init__(self, rootValue):
        self.tree = []
        self.tree.append(Node(rootValue, None, 0)) #Creates the parent node of the tree with value rootValue

    def findRoot(self):
        for node in range(len(self.tree)):
            if self.tree[node].parent == None:
                return self.tree[node] #Returns node in tree with no parent (the root node)

    def addNode(self, value, parent):
        idx = len(self.tree)
        self.tree.append(Node(value, parent, idx))
        self.tree[self.tree[-1].parent].addChild(value, idx) #Adds child index to parent node's children list
        
"""Run after every deletion. Checks each node in the tree and updates it and it's parent to keep track of the node's position in the
unordered tree list."""
    def updateIdx(self, idx):
        for node in range(len(self.tree)):
            if node > idx:
                self.tree[node].treeIdx -= 1
            try:
                if self.tree[node].parent > idx:
                    self.tree[node].parent -= 1
            except TypeError:
                pass
            try:
                for child in self.tree[node].children:
                    if child > idx:
                        child -= 1
            except TypeError:
                pass

    def delNode(self, value): #Deletes node with value = 'value'
        for node in range(len(self.tree)):
            if self.tree[node].value == value:
                idx = self.tree[node].treeIdx
                break

#If the node has no children, remove the node from its parent's children list and delte it from the tree.
        if self.tree[idx].children == [None, None]:
            self.tree[self.tree[idx].parent].killChild(idx)
            del self.tree[idx]
            self.updateIdx(idx)

"""If the node has two children, the minimum value in the right subtree is located and copied into the node
called for deletion. The node with the minimum value is then deleted."""
        elif self.tree[idx].children[0] != None and self.tree[idx].children[1] \
        != None:
            minVal = self.tree[idx].children[1] #Starts search in right subtree
            while True:
                if self.tree[minVal].children == [None, None]: #Checks for leaf node (minimum value)
                    break

                if self.tree[minVal].children[0] != None:
                    minVal = self.tree[minVal].children[0]
                else:
                    minVal = self.tree[minVal].children[1]
            self.tree[idx].value = self.tree[minVal].value #The value is copied into node for deletion
            self.tree[self.tree[minVal].parent].killChild(minVal)
            del self.tree[minVal] #The leaf node is then deleted
            self.updateIdx(minVal)

#If the node has one child, copy the child's value into the node to delete and delete the child from the tree.
        else:
            for child in self.tree[idx].children:
                if child != None:
                    self.tree[idx].value = self.tree[child].value
                    self.tree[idx].killChild(self.tree[child].treeIdx)
                    del self.tree[child]
                    self.updateIdx(child)
                    
"""To search the binary tree, we check if value is found, if not, we compare the current value to the target
value and move to the left or right child depending on whether the current value is larger/smaller than the
target."""
    def searchNode(self, value):
        path = []
        current = self.findRoot() #Starts at the root node

        while True:
            if current.value == value: #Checks if current value = target value and breaks if true
                break
            elif value < current.value:
                targetChild = 0
                path.append('left') #If the current value is greater than the target value, move to the left subtree and add 'left' to the search path
            else:
                targetChild = 1 #If the current value is lesser than the target value, move to the right subtree and add 'right' to the search path
                path.append('right')

            if current.children[targetChild] == None:
                print('Target not found!') #If the current value is not the target and is a leaf node, print 'not found'.
                del path[-1]
                break
            else:
                current = self.tree[current.children[targetChild]]

        if path == []: #If the target value was the inital value then the target was the root node, with no path
            print('Location: ROOT')
        else:
            print('Location: ' + str(path)) #Prints the path out as a list with each individual left/right movement in order

"""As each type of binary tree traversal requires recursion, the runTraversal() function manages the traversal
order that is handed to the user and prints it once the traversal algorithm has completed."""
    def runTraversal(self, traversal):
        self.traversalOrder = []
        if traversal == 'preOrder':
            self.preOrderTraversal(self.findRoot().treeIdx)
        elif traversal == 'inOrder':
            self.inOrderTraversal(self.findRoot().treeIdx)
        elif traversal == 'postOrder':
            self.postOrderTraversal(self.findRoot().treeIdx)

        print(self.traversalOrder)


    def preOrderTraversal(self, node):
        if self.tree[node] not in self.traversalOrder:
            self.traversalOrder.append(self.tree[node].value) #Add value to traversal order

        for child in range(2): #Traverse each subtree, starting with the left (children[0]).
            if self.tree[node].children[child] not in self.traversalOrder and \
            self.tree[node].children[child] != None:
                self.preOrderTraversal(self.tree[self.tree[node].children[child]].treeIdx)

    def inOrderTraversal(self, node):
        if self.tree[node].children[0] not in self.traversalOrder and \
        self.tree[node].children[0] != None:
            self.inOrderTraversal(self.tree[self.tree[node].children[0]].treeIdx) #Traverse left subtree

        if self.tree[node].children == [None, None] or \
        self.tree[self.tree[node].children[0]].value in self.traversalOrder:
            self.traversalOrder.append(self.tree[node].value) #Add node value to traversal order starting at leaf

        if self.tree[node].children[1] not in self.traversalOrder and \
        self.tree[node].children[1] != None:
            self.inOrderTraversal(self.tree[self.tree[node].children[1]].treeIdx) #Traverse right subtree

    def postOrderTraversal(self, node):
        if self.tree[node].children[0] not in self.traversalOrder and \
        self.tree[node].children[0] != None:
            self.postOrderTraversal(self.tree[self.tree[node].children[0]].treeIdx) #Traverse left subtree

        if self.tree[node].children[1] not in self.traversalOrder and \
        self.tree[node].children[1] != None:
            self.postOrderTraversal(self.tree[self.tree[node].children[1]].treeIdx) #Traverse right subtree

        if (self.tree[node].children == [None, None]) or \
        (self.tree[node].children[0] != None and self.tree[node].children[1] != \
        None and self.tree[self.tree[node].children[0]].value in self.traversalOrder\
        and self.tree[self.tree[node].children[1]].value in self.traversalOrder):
            self.traversalOrder.append(self.tree[node].value) #Add node value to traversal order starting at leaf

        else:
            for child in range(2):
                if self.tree[node].children[child] != None:
                    if self.tree[self.tree[node].children[child]].value in \
                    self.traversalOrder:
                        self.traversalOrder.append(self.tree[node].value)
