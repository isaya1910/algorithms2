class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        vertex = Vertex(v)
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = vertex
                return

    def RemoveVertex(self, v):
        self.vertex[v] = None
        for i in range(self.max_vertex):
            self.m_adjacency[i][v] = 0
            self.m_adjacency[v][i] = 0


    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom, VTo):
        stack = []
        for v in self.vertex:
            if v is not None:
                v.Hit = False

        vStart  = self.vertex[VFrom]
        stack.append(vStart)

        while len(stack) !=0:
            ver = stack[-1]
            vi = self.vertex.index(ver)
            ver.Hit = True

            isFind = False
            for i in range(self.max_vertex):
                if self.m_adjacency[vi][i] == 1 and self.vertex[i].Hit == False:
                    stack.append(self.vertex[i])
                    isFind = True
                    if i == VTo:
                        return stack
                    break

            if isFind == False:
                stack.pop()

        return stack






