class Node():
    def __init__(self, value, parent, treeIdx):
        self.value = value
        self.parent = parent
        self.children = [None, None]
        self.treeIdx = treeIdx

    def addChild(self, childValue, childIdx):
        if childValue < self.value:
            self.children[0] = childIdx
        else:
            self.children[1] = childIdx

    def killChild(self, childIdx):
        for child in range(len(self.children)):
            if self.children[child] == childIdx:
                self.children[child] = None

    def setParent(self, parentIdx):
        self.parent = parentIdx



class Tree():
    def __init__(self, rootValue):
        self.tree = []
        self.tree.append(Node(rootValue, None, 0))
        self.traversalOrder = []

    def findRoot(self):
        for node in range(len(self.tree)):
            if self.tree[node].parent == None:
                return self.tree[node]

    def addNode(self, value, parent):
        idx = len(self.tree)
        self.tree.append(Node(value, parent, idx))
        self.tree[self.tree[-1].parent].addChild(value, idx)

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

    def delNode(self, value):
        for node in range(len(self.tree)):
            if self.tree[node].value == value:
                idx = self.tree[node].treeIdx
                break

        if self.tree[idx].children == [None, None]:
            self.tree[self.tree[idx].parent].killChild(idx)
            del self.tree[idx]
            self.updateIdx(idx)

        elif self.tree[idx].children[0] != None and self.tree[idx].children[1] \
        != None:
            minVal = self.tree[idx].children[1]
            while True:
                if self.tree[minVal].children == [None, None]:
                    break

                if self.tree[minVal].children[0] != None:
                    minVal = self.tree[minVal].children[0]
                else:
                    minVal = self.tree[minVal].children[1]
            self.tree[idx].value = self.tree[minVal].value
            self.tree[self.tree[minVal].parent].killChild(minVal)
            del self.tree[minVal]
            self.updateIdx(minVal)

        else:
            for child in self.tree[idx].children:
                if child != None:
                    self.tree[idx].value = self.tree[child].value
                    self.tree[idx].killChild(self.tree[child].treeIdx)
                    del self.tree[child]
                    self.updateIdx(child)

    def searchNode(self, value):
        path = []
        target = self.findRoot()

        while True:
            if target.value == value:
                break
            elif value < target.value:
                targetChild = 0
            else:
                targetChild = 1

            if target.children[targetChild] == None:
                print('Target not found!')
                break
            else:
                target = self.tree[target.children[targetChild]]

        if path == []:
            print('Location: ROOT')
        else:
            print('Location: '', '.join(path))

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
            self.traversalOrder.append(self.tree[node].value)

        for child in range(2):
            if self.tree[node].children[child] not in self.traversalOrder and \
            self.tree[node].children[child] != None:
                self.preOrderTraversal(self.tree[self.tree[node].children[child]].treeIdx)

    def inOrderTraversal(self, node):
        if self.tree[node].children[0] not in self.traversalOrder and \
        self.tree[node].children[0] != None:
            self.inOrderTraversal(self.tree[self.tree[node].children[0]].treeIdx)

        if self.tree[node].children == [None, None] or \
        self.tree[self.tree[node].children[0]].value in self.traversalOrder:
            self.traversalOrder.append(self.tree[node].value)

        if self.tree[node].children[1] not in self.traversalOrder and \
        self.tree[node].children[1] != None:
            self.inOrderTraversal(self.tree[self.tree[node].children[1]].treeIdx)

    def postOrderTraversal(self, node):
        if self.tree[node].children[0] not in self.traversalOrder and \
        self.tree[node].children[0] != None:
            self.postOrderTraversal(self.tree[self.tree[node].children[0]].treeIdx)

        if self.tree[node].children[1] not in self.traversalOrder and \
        self.tree[node].children[1] != None:
            self.postOrderTraversal(self.tree[self.tree[node].children[1]].treeIdx)

        if (self.tree[node].children == [None, None]) or \
        (self.tree[node].children[0] != None and self.tree[node].children[1] != \
        None and self.tree[self.tree[node].children[0]].value in self.traversalOrder\
        and self.tree[self.tree[node].children[1]].value in self.traversalOrder):
            self.traversalOrder.append(self.tree[node].value)

        else:
            for child in range(2):
                if self.tree[node].children[child] != None:
                    if self.tree[self.tree[node].children[child]].value in \
                    self.traversalOrder:
                        self.traversalOrder.append(self.tree[node].value)

tree = Tree(47)
tree.addNode(21, 0)
tree.addNode(52, 0)
tree.addNode(11, 1)
tree.addNode(28, 1)
tree.addNode(25, 4)
tree.addNode(33, 4)
tree.addNode(30, 6)
tree.addNode(41, 6)
tree.addNode(51, 2)
tree.addNode(66, 2)

tree.runTraversal('postOrder')