import unittest

from heap import Heap

class HeapTest(unittest.TestCase):
    def testAdd(self):
        testObject = Heap()
        testObject.MakeHeap([],3)

        testObject.Add(7)
        testObject.Add(9)
        testObject.Add(12)

        self.assertEqual(testObject.HeapArray[0], 12)

