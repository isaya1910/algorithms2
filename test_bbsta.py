import unittest

from bbsta import GenerateBBSTArray

class BBSTATest(unittest.TestCase):

    def test(self):
        testList = [8,-5,6,3,16,2,7,9]
        # -5, 2, 3, 6, 7, 8 , 9 , 16
        #  0, 1, 2, 3, 4, 5,  6,  7


        result = GenerateBBSTArray(testList)
        print(result)
        self.assertEqual(len(result), 15)
        self.assertEqual(testList[0],-5)

        self.assertEqual(result[0],6)
        self.assertEqual(result[1],2)
        self.assertEqual(result[2], 8)
        self.assertEqual(result[3],-5)
        self.assertEqual(result[4], 3)

        testList2 = [18, 10]
        result = GenerateBBSTArray(testList2)
        self.assertEqual(result[0],10)
        self.assertEqual(result[2], 18)

        result = GenerateBBSTArray([])
        self.assertEqual(len(result),0)

    def test2(self):

        testList2 = [18, 10]
        result = GenerateBBSTArray(testList2)
        self.assertEqual(result[0],10)
        self.assertEqual(result[2], 18)

        result = GenerateBBSTArray([])
        self.assertEqual(len(result),0)
