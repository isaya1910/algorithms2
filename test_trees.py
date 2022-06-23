import unittest


from trees import SimpleTreeNode, SimpleTree

class SimpleTreeNodeTest(unittest.TestCase):
    def testAddChild(self):
        parentNode =  SimpleTreeNode(19, None)
        childNode = SimpleTreeNode(5, None)

        testObject = SimpleTree(parentNode)
        testObject.AddChild(parentNode, childNode)

        self.assertEqual(len(parentNode.Children),1)

    def testDeleteNode(self):
        parentNode =  SimpleTreeNode(19, None)
        childNode = SimpleTreeNode(5, None)
        testObject = SimpleTree(parentNode)
        testObject.AddChild(parentNode,childNode)
        testObject.DeleteNode(childNode)
        self.assertEqual(len(parentNode.Children),0)
        self.assertIsNone(childNode.Parent)

    def testGetAllNodes(self):
        parentNode =  SimpleTreeNode(19, None)
        testObject = SimpleTree(parentNode)
        for i in range(6):
            testObject.AddChild(parentNode, SimpleTreeNode(i,parentNode))
        for node in parentNode.Children:
            testObject.AddChild(node, SimpleTreeNode(12, node))
        self.assertEqual(len(parentNode.Children), 6)
        allNodes = testObject.GetAllNodes()
        self.assertEqual(len(allNodes),13)

    def testFindAllNotesByValue(self):
        parentNode = SimpleTreeNode(1, None)
        testObject = SimpleTree(parentNode)
        for i in range(10):
            testObject.AddChild(parentNode, SimpleTreeNode(i, parentNode))
        firstChildNode = parentNode.Children[0]
        testObject.AddChild(firstChildNode, SimpleTreeNode(1, parentNode))

        ansList = testObject.FindNodesByValue(1)

        self.assertEqual(len(ansList), 3)

    def testMoveNode(self):
        parentNode = SimpleTreeNode(1, None)
        testObject = SimpleTree(parentNode)
        childNode1 = SimpleTreeNode(3, parentNode)
        childNode2 = SimpleTreeNode(4, parentNode)

        childNode1_1 = SimpleTreeNode(5, childNode1)

        testObject.AddChild(parentNode, childNode1)
        testObject.AddChild(parentNode, childNode2)

        testObject.AddChild(childNode1, childNode1_1)

        self.assertEqual(len(childNode1.Children), 1)

        testObject.MoveNode(childNode1_1, childNode2)

        self.assertEqual(len(childNode2.Children),1)
        self.assertEqual(len(childNode1.Children),0)

    def testCount(self):
        parentNode = SimpleTreeNode(1, None)
        testObject = SimpleTree(parentNode)

        for i in range(20):
            testObject.AddChild(parentNode, SimpleTreeNode(i, parentNode))

        self.assertEqual(testObject.Count(), 21)
        self.assertEqual(testObject.LeafCount(), 20)
