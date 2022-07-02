import unittest

from abst import aBST

class aBSTTest(unittest.TestCase):
    def testInit(self):
        testObject = aBST(3)
        self.assertEqual(len(testObject.Tree), 16)

    def testFindIndexByKey(self):
        testObject = aBST(3)
        testObject.Tree[0] = 1
        testObject.Tree[1] = -5
        testObject.Tree[2] = 5

        self.assertEqual(testObject.FindKeyIndex(5), 2)

        self.assertEqual(testObject.FindKeyIndex(8), -6)

    def testAddKey(self):
        testObject = aBST(2)

        testObject.AddKey(1)

        self.assertEqual(testObject.Tree[0], 1)

        testObject.AddKey(7)
        testObject.AddKey(-3)

        self.assertEqual(testObject.Tree[1],-3)
        self.assertEqual(testObject.Tree[2], 7)

        self.assertEqual(testObject.AddKey(-2), 4)

        self.assertEqual(testObject.Tree[4],-2)
        self.assertEqual(testObject.AddKey(5), 5)
        self.assertEqual(testObject.AddKey(8),6)

        self.assertEqual(testObject.Tree[5], 5)
        self.assertEqual(testObject.Tree[6],8)

        self.assertEqual(testObject.AddKey(-10), 3)
        self.assertEqual(testObject.AddKey(-12),7)

        self.assertEqual(testObject.AddKey(-100),-1)

    def testEdgeCases(self):
        testObject = aBST(0)
        testObject.AddKey(1)
        self.assertEqual(testObject.Tree[0],1)

        self.assertEqual(testObject.AddKey(2),-1)
        self.assertEqual(testObject.AddKey(1),0)

    def testEdgeCases2(self):
        testObject = aBST(0)
        self.assertEqual(testObject.AddKey(4),0)
        self.assertEqual(testObject.AddKey(8),-1)



