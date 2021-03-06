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


    def clearVisited(self):
        for v in self.vertex:
            if v is not None:
                v.Hit = False

    def BreadthFirstSearch(self, VFrom, VTo):
        path = []
        queue = []
        self.clearVisited()
        vStart = self.vertex[VFrom]
        path.append(vStart)

        queue.append(path.copy())

        while len(queue) != 0:
            path = queue.pop(0)
            ver = path[-1]
            vi = self.vertex.index(ver)
            ver.Hit = True
            if vi == VTo:
                return path
            for i in range(self.max_vertex):
                if self.m_adjacency[vi][i] == 1 and self.vertex[i].Hit == False:
                    newPath = path.copy()
                    newPath.append(self.vertex[i])
                    queue.append(newPath)
        return []

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

    def WeakVertices(self):
        # ???????????????????? ???????????? ?????????? ?????? ??????????????????????????

        strongVertices = [False]* self.max_vertex
        for i in range(self.max_vertex):
            if strongVertices[i] == True:
                continue
            for j in range(self.max_vertex):
                if self.m_adjacency[i][j] == 1 and i!=j:
                    for z in range(self.max_vertex):
                        if self.m_adjacency[j][z] == 1 and self.m_adjacency[i][z] == 1 and i!=j and i!=z and j!=z:
                            strongVertices[i] = True
                            strongVertices[j] = True
                            strongVertices[z] = True

        edges = []
        for i in range(self.max_vertex):
            if strongVertices[i] == False:
                edges.append(self.vertex[i])
        return edges

