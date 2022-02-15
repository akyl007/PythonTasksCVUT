class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.minDistance = float('inf')
        self.previousVertex = None
        self.visited = False
        self.edges = []

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self):
        self.vertices_list = []

    def computePath(self, sourceId):
        queue = []

        for vertex in self.vertices_list:
            if (sourceId == vertex.id):
                vertex.minDistance = 0
                queue.insert(0, vertex)
            else:
                queue.append(vertex)

        while queue:
            vertex = queue.pop(0)
            for current_edge in vertex.edges:
                tTarget = current_edge.target
                for main_vertex in self.vertices_list:
                    if (main_vertex.id == tTarget):
                        if (main_vertex.minDistance > (vertex.minDistance + current_edge.weight)):
                            main_vertex.minDistance = vertex.minDistance + current_edge.weight
                            main_vertex.previousVertex = vertex
            for element in range(len(queue)):
                try:
                    if (queue[element].minDistance > queue[element + 1].minDistance):
                        el = queue[element + 1]
                        queue[element + 1] = queue[element]
                        queue[element] = el
                except IndexError:
                    break

    def getShortestPathTo(self, targetId):
        vertices = []

        for vertex in self.vertices_list:
            if (vertex.id == targetId):
                tTarget = vertex
                vertices.append(tTarget)

        for vertex in self.vertices_list:
            if (vertex == tTarget.previousVertex):
                vertices.append(vertex)
                tTarget = tTarget.previousVertex
        vertices.reverse()
        return vertices

    def createGraph(self, vertexes, edgesToVertexes):
        self.vertices_list = vertexes
        for vertex in vertexes:
            for current_edge in edgesToVertexes:
                if (current_edge.source == vertex.id):
                    vertex.edges.append(current_edge)

    def resetDijkstra(self):
        for vertex in self.vertices_list:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None

    def getVertexes(self):
        return self.vertices_list