class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        parent = NodeToDelete.Parent
        NodeToDelete.Parent = None
        parent.Children.remove(NodeToDelete)

    def TraverseByAllNodes(self, root, allNodes):
        if len(root.Children)== 0:
            allNodes.append(root)
            return allNodes
        allNodes.append(root)
        for node in root.Children:
            self.TraverseByAllNodes(node, allNodes)
        return allNodes

    def GetAllNodes(self):
        ans  = []
        self.TraverseByAllNodes(self.Root, ans)
        return ans

    def FindNodesByValue(self, val):
        allNodes = []
        self.TraverseByAllNodes(self.Root, allNodes)
        ans = []
        for node in allNodes:
            if node.NodeValue == val:
                ans.append(node)
        return ans

    def MoveNode(self, OriginalNode, NewParent):
        oldParent = OriginalNode.Parent
        oldParent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        return self.countLeafs(self.Root)

    def countLeafs(self, node):
        if len(node.Children) == 0:
            return 1

        ans = 0
        for child in node.Children:
            ans += self.countLeafs(child)
        return ans



