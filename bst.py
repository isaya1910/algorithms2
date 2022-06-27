class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None
        self.NodeCount = 1

    def findNodeByKey(self, node, key):
        if node.NodeKey == key:
            bstFind = BSTFind()
            bstFind.Node = node
            bstFind.NodeHasKey = True
            return bstFind

        leftChild = node.LeftChild
        rightChild = node.RightChild

        if node.NodeKey > key:
            if leftChild is None:
                bstFind = BSTFind()
                bstFind.Node = node
                bstFind.NodeHasKey = False
                bstFind.ToLeft = True
                return bstFind
            else:
                return self.findNodeByKey(leftChild, key)
        else:
            if rightChild is None:
                bstFind = BSTFind()
                bstFind.Node = node
                bstFind.NodeHasKey = False
                bstFind.ToLeft = False
                return bstFind
            else:
                return self.findNodeByKey(rightChild, key)

    def FindNodeByKey(self, key):
        if self.Root is None:
            return BSTFind()
        return self.findNodeByKey(self.Root,key)

    def AddKeyValue(self, key, val):
        bstFind = self.FindNodeByKey(key)
        if bstFind.Node is None:
            self.Root = BSTNode(key, val, None)
            self.NodeCount = 1
            return True
        if bstFind.NodeHasKey == True:
            return False
        if bstFind.ToLeft == True:
            bstFind.Node.LeftChild = BSTNode(key,val,bstFind.Node)
        else:
            bstFind.Node.RightChild = BSTNode(key,val,bstFind.Node)
        self.NodeCount += 1
        return True

    def FinMinMax(self, FromNode, FindMax):
        if FindMax == False:
            if FromNode.LeftChild == None:
                return FromNode
            else:
                return self.FinMinMax(FromNode.LeftChild, FindMax)
        else:
            if FromNode.RightChild == None:
                return FromNode
            else:
                return self.FinMinMax(FromNode.RightChild, FindMax)

    def DeleteNodeByKey(self, key):
        bstFind = self.FindNodeByKey(key)
        if bstFind.NodeHasKey == False:
            return False

        self.NodeCount -= 1
        nodeToDelete = bstFind.Node
        parent = nodeToDelete.Parent

        if parent is None:
            if nodeToDelete.LeftChild is None and nodeToDelete.RightChild is None:
                self.Root = None
                return True
            if nodeToDelete.RightChild is not None and nodeToDelete.LeftChild is not None:
                rightChild = nodeToDelete.RightChild
                candidate = self.FinMinMax(rightChild, False)
                self.Root = candidate
                nodeToDelete.LeftChild.Parent = candidate
                return True
            if nodeToDelete.RightChild is None:
                self.Root = nodeToDelete.LeftChild
                return True
            if nodeToDelete.LeftChild is None:
                self.Root = nodeToDelete.RightChild
                return True

        if nodeToDelete.LeftChild is None and nodeToDelete.RightChild is None:
            if parent.LeftChild is nodeToDelete:
                parent.LeftChild = None
            else:
                parent.RightChild = None
            return True

        if nodeToDelete.LeftChild is not None and nodeToDelete.RightChild is not None:
            rightChild = nodeToDelete.RightChild
            candidate = self.FinMinMax(rightChild, False)
            if parent.LeftChild is nodeToDelete:
                parent.LeftChild = candidate
            else:
                parent.RightChild = candidate
            candidate.Parent = parent
            return True

        if nodeToDelete.LeftChild is not None:
            if parent.LeftChild.NodeKey ==  nodeToDelete.NodeKey:
                parent.LeftChild = nodeToDelete.LeftChild
            else:
                parent.RightChild = nodeToDelete.LeftChild

            nodeToDelete.LeftChild.Parent = parent
            return True

        if nodeToDelete.RightChild is not None:
            if parent.RightChild.NodeKey == nodeToDelete.NodeKey:
                parent.RightChild = nodeToDelete.RightChild
            else:
                parent.LeftChild  = nodeToDelete.RightChild
            nodeToDelete.RightChild.Parent = parent
            return True


    def Count(self):
        return self.NodeCount
