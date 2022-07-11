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

    def testEvenTrees(self):

        parentNode = SimpleTreeNode(1, None)

        testObject = SimpleTree(parentNode)

        child6 = SimpleTreeNode(6, parentNode)
        testObject.AddChild(parentNode, child6)

        child3 = SimpleTreeNode(3, parentNode)
        testObject.AddChild(parentNode,child3)

        child2 = SimpleTreeNode(2, parentNode)
        testObject.AddChild(parentNode,child2)

        child8 = SimpleTreeNode(8, child6)
        testObject.AddChild(child6, child8)

        child9 = SimpleTreeNode(9, child8)
        testObject.AddChild(child8, child9)

        child10 = SimpleTreeNode(10, child8)
        testObject.AddChild(child8, child10)

        child4 = SimpleTreeNode(4, child3)
        testObject.AddChild(child3, child4)

        child5 = SimpleTreeNode(5, child2)
        testObject.AddChild(child2, child5)

        child7 = SimpleTreeNode(7, child2)
        testObject.AddChild(child2, child7)

        actual = testObject.EvenTrees()

        self.assertEqual(len(actual), 4)
        self.assertEqual(actual[0], parentNode)
        self.assertEqual(actual[1], child6)
        self.assertEqual(actual[2], parentNode)
        self.assertEqual(actual[3], child3)



