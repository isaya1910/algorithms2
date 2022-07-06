import unittest

from heap import Heap

class HeapTest(unittest.TestCase):
    def testAdd(self):
        testObject = Heap()
        testObject.MakeHeap([12,3,4,9],3)


        self.assertEqual(testObject.GetMax(), 12)
        self.assertEqual(testObject.GetMax(), 9)
        self.assertEqual(testObject.GetMax(), 4)
        self.assertEqual(testObject.GetMax(), 3)
        self.assertEqual(testObject.GetMax(), -1)

