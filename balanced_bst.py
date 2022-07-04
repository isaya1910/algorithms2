class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла

class BalancedBST:

    def __init__(self):
    	self.Root = None # корень дерева

    def generateBBSTArray(self, initial_array, parent,height):

        if not initial_array:
            return None

        mid_index = (len(initial_array))//2

        node  = BSTNode(initial_array[mid_index], parent)
        node.Level = height
        node.LeftChild = self.generateBBSTArray(initial_array[:mid_index], node, height + 1)
        node.RightChild = self.generateBBSTArray(initial_array[mid_index + 1:], node,  height + 1)
        return node

    def GenerateTree(self, a):
        a.sort()
        self.Root = self.generateBBSTArray(a,None,0)

    def height(self, root):

        if root is None:
            return 0
        return max(self.height(root.LeftChild), self.height(root.RightChild)) + 1
    def IsBalanced(self, root_node):
        if root_node is None:
            return True

        lh = self.height(root_node.LeftChild)
        rh = self.height(root_node.RightChild)

        if (abs(lh - rh) <= 1) and self.IsBalanced(root_node.LeftChild) is True and self.IsBalanced(root_node.RightChild) is True:
            return True

        return False
