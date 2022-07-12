import unittest

from graph import Vertex, SimpleGraph

class GraphTest(unittest.TestCase):

    def testAddVertex(self):
        testObject = SimpleGraph(5)
        testObject.AddVertex(8)

        self.assertIsNotNone(testObject.vertex[0])

    def testDeleteVertex(self):
        testObject = SimpleGraph(5)
        testObject.AddVertex(8)

        self.assertIsNotNone(testObject.vertex[0])

        testObject.RemoveVertex(0)
        self.assertIsNone(testObject.vertex[0])

    def testAddEdge(self):

        testObject = SimpleGraph(5)
        testObject.AddVertex(8)
        testObject.AddVertex(10)

        testObject.AddEdge(0,1)
        self.assertEqual(testObject.IsEdge(0,1), True)
        self.assertEqual(testObject.IsEdge(1,0), True)

        testObject.RemoveVertex(0)

        self.assertEqual(testObject.IsEdge(0,1), False)
        self.assertEqual(testObject.IsEdge(1,0), False)

    def testDFS(self):
        testObject = SimpleGraph(5)

        testObject.AddVertex(8)

        testObject.AddVertex(10)

        testObject.AddVertex(9)

        testObject.AddEdge(0,1)

        actual = testObject.DepthFirstSearch(0,1)

        self.assertEqual(actual[0].Value, 8)

        self.assertEqual(actual[1].Value, 10)

        actual = testObject.DepthFirstSearch(0,2)
        self.assertEqual(len(actual),0)


        testObject.AddVertex(12)

        testObject.AddEdge(1,3)

        actual = testObject.DepthFirstSearch(0,3)

        self.assertEqual(len(actual), 3)

        self.assertEqual(actual[0].Value, 8)

        self.assertEqual(actual[1].Value, 10)

        self.assertEqual(actual[2].Value, 12)
