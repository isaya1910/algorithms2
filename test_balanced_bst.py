import unittest

from balanced_bst import BSTNode, BalancedBST

class BalancedBSTTest(unittest.TestCase):
    def testGenerateTree(self):
        testObject = BalancedBST()
        testObject.GenerateTree([1,8,9])
        self.assertEqual(testObject.Root.NodeKey, 8)
        self.assertEqual(testObject.Root.RightChild.NodeKey, 9)
        self.assertEqual(testObject.Root.LeftChild.NodeKey, 1)
        self.assertEqual(testObject.IsBalanced(testObject.Root), True)

        rightChild = testObject.Root.RightChild

        rightChild.RightChild = BSTNode(10, rightChild)

        rightChild2 = rightChild.RightChild

        rightChild2.RightChild = BSTNode(12, rightChild2)
        self.assertEqual(testObject.IsBalanced(testObject.Root), False)
