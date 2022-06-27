
import unittest


from bst import BSTNode, BSTFind, BST

class BSTTest(unittest.TestCase):

    def testFindNodeByKey(self):
        root = BSTNode(1,1,None)
        testObject = BST(root)
        result = testObject.FindNodeByKey(1)
        self.assertEqual(result.NodeHasKey, True)
        result1 = testObject.FindNodeByKey(3)

        self.assertEqual(result1.NodeHasKey, False)

        root.RightChild = BSTNode(5,5, root)
        root.LeftChild = BSTNode(-10,-10, root)

        result3 = testObject.FindNodeByKey(-10)
        self.assertEqual(result3.NodeHasKey, True)

        result4 = testObject.FindNodeByKey(-120)
        self.assertEqual(result4.NodeHasKey, False)
        self.assertEqual(result4.ToLeft, True)

        result5 = testObject.FindNodeByKey(100)
        self.assertEqual(result5.NodeHasKey, False)
        self.assertEqual(result5.ToLeft, False)

    def testAdditionAddKeyValue(self):

        root = BSTNode(1, 1, None)
        testObject = BST(root)
        self.assertEqual(testObject.Count(),1)
        self.assertEqual(testObject.DeleteNodeByKey(1),True)
        self.assertEqual(testObject.Count(),0)
        self.assertIsNone(testObject.Root)
        self.assertEqual(testObject.AddKeyValue(1,1),True)
        self.assertEqual(testObject.Count(),1)
        self.assertEqual(testObject.Root.NodeKey,1)

    def testAddKeyValue(self):
        root = BSTNode(1, 1, None)
        testObject = BST(root)

        self.assertEqual(testObject.AddKeyValue(3,3), True)
        self.assertIsNotNone(testObject.Root.RightChild)

        self.assertEqual(testObject.AddKeyValue(3,3), False)
        self.assertEqual(testObject.AddKeyValue(-1,-1),True)
        self.assertIsNotNone(testObject.Root.LeftChild)

    def testFinMinMax(self):
        root = BSTNode(1, 1, None)
        testObject = BST(root)
        testObject.AddKeyValue(-10,-10)
        testObject.AddKeyValue(-100,20)
        testObject.AddKeyValue(10, 10)
        testObject.AddKeyValue(100,100)
        self.assertEqual(testObject.FinMinMax(testObject.Root, True).NodeKey,100)
        self.assertEqual(testObject.FinMinMax(testObject.Root, False).NodeKey,-100)

    def testDelete(self):
        root = BSTNode(1, 1, None)
        testObject = BST(root)
        self.assertEqual(testObject.Count(),1)
        self.assertEqual(testObject.DeleteNodeByKey(-1), False)
        testObject.AddKeyValue(-1,-1)
        self.assertEqual(testObject.Count(),2)
        self.assertEqual(testObject.Root.LeftChild.NodeKey, -1)
        testObject.AddKeyValue(100,100)
        self.assertEqual(testObject.Count(),3)
        self.assertEqual(testObject.Root.RightChild.NodeKey, 100)

        self.assertEqual(testObject.DeleteNodeByKey(-1),True)
        self.assertIsNone(testObject.Root.LeftChild)
        self.assertEqual(testObject.Count(),2)
        self.assertEqual(testObject.DeleteNodeByKey(100), True)
        self.assertIsNone(testObject.Root.RightChild)
        self.assertEqual(testObject.Count(),1)

        testObject.AddKeyValue(100,100)
        testObject.AddKeyValue(200,200)

        self.assertEqual(testObject.DeleteNodeByKey(100), True)
        self.assertEqual(testObject.Root.RightChild.NodeKey, 200)

        testObject.AddKeyValue(-100,-100)
        testObject.AddKeyValue(-200, -200)

        self.assertEqual(testObject.DeleteNodeByKey(-100), True)
        self.assertEqual(testObject.Root.LeftChild.NodeKey, -200)

        self.assertEqual(testObject.DeleteNodeByKey(-200), True)
        self.assertIsNone(testObject.Root.LeftChild)

    def testDeleteNodeWithTwoChilds(self):
        root = BSTNode(1,1,None)
        testObject = BST(root)

        testObject.AddKeyValue(10,10)

        testObject.AddKeyValue(12,12)
        testObject.AddKeyValue(8,8)

        testObject.AddKeyValue(11,11)
        self.assertEqual(testObject.Root.RightChild.NodeKey, 10)
        testObject.DeleteNodeByKey(10)
        self.assertEqual(testObject.Root.RightChild.NodeKey, 11)
        testObject.AddKeyValue(10,10)
        testObject.AddKeyValue(5,5)
        testObject.AddKeyValue(-1,-1)
        testObject.DeleteNodeByKey(1)
        self.assertEqual(testObject.Root.NodeKey, 5)

    def testCount(self):
        root = BSTNode(1,1,None)
        testObject = BST(root)
        self.assertEqual(testObject.Count(),1)
        testObject.AddKeyValue(2,2)
        self.assertEqual(testObject.Count(),2)
        testObject.DeleteNodeByKey(2)
        self.assertEqual(testObject.Count(),1)
        testObject.DeleteNodeByKey(1)
        self.assertEqual(testObject.Count(),0)
