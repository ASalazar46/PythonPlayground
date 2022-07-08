# -----
# -----
# Graphs
# -----
# -----

# Undirected, unweighted graph represented with a dictionary
class Graph1:
    def __init__(self, existGraph=None):
        if existGraph == None:
            self.adjDict = {}
        else:
            self.adjDict = existGraph
    
    def add_vertex(self, vertexKey):
        if vertexKey not in self.adjDict:
            self.adjDict[vertexKey] = []

    def add_edge(self, fromVertexKey, toVertexKey):
        if toVertexKey not in self.adjDict[fromVertexKey]:
            self.adjDict[fromVertexKey].append(toVertexKey)
            self.adjDict[toVertexKey].append(fromVertexKey)

    def print_vertices(self):
        print(list(self.adjDict.keys()))

    def print_edges(self):
        edgeList = []
        for vertexKey in self.adjDict:
            for vertexValue in self.adjDict[vertexKey]:
                if {vertexValue, vertexKey} not in edgeList:
                    edgeList.append({vertexValue, vertexKey})
        print(edgeList)

# Directed, unweighted graph represented with a dictionary
class Graph2:
    def __init__(self, existGraph=None):
        if existGraph == None:
            self.adjDict = {}
        else:
            self.adjDict = existGraph
    
    def add_vertex(self, vertexKey):
        if vertexKey not in self.adjDict:
            self.adjDict[vertexKey] = []

    def add_edge(self, fromVertexKey, toVertexKey):
        if toVertexKey not in self.adjDict[fromVertexKey]:
            self.adjDict[fromVertexKey].append(toVertexKey)

    def print_vertices(self):
        print(list(self.adjDict.keys()))

    def print_edges(self):
        edgeList = []
        for vertexKey in self.adjDict:
            for vertexValue in self.adjDict[vertexKey]:
                    edgeList.append((vertexKey, vertexValue))
        print(edgeList)

# Undirected, weighted graph represented with a 2d list / adjacency matrix
class Graph3:
    def __init__(self, vrtCnt):
        self.adjMat = [[-1]*vrtCnt for x in range(vrtCnt)]
        self.vertices = {x for x in range(vrtCnt)}
        self.vrtCnt = vrtCnt
    
    def add_vertex(self):
        self.vertices.add(self.vrtCnt)
        self.vrtCnt += 1
        for adjacencies in self.adjMat:
            adjacencies.append(-1)
        self.adjMat.append([-1]*self.vrtCnt)
        print('Vertex {0} added.'.format(self.vrtCnt-1))

    def add_edge(self, vrtFrom, vrtTo, weight=0):
        self.adjMat[vrtFrom][vrtTo] = weight
        self.adjMat[vrtTo][vrtFrom] = weight
        print('Edge from {0} to {1} of weight {2} added.'.format(vrtFrom, vrtTo, weight))
        print('Edge from {0} to {1} of weight {2} added.'.format(vrtTo, vrtFrom, weight))

    def print_vertices(self):
        print('-'*50)
        print('Printing vertices...')
        print(self.vertices)
        print('-'*50)

    def print_edges(self):
        print('-'*50)
        print('Printing edges...')
        for vrtFrom in range(self.vrtCnt):
            for vrtTo in range(self.vrtCnt):
                if self.adjMat[vrtFrom][vrtTo] != -1:
                    print((vrtFrom, vrtTo, self.adjMat[vrtFrom][vrtTo]))
        print('-'*50)

# Directed, weighted graph represented with a 2d list / adjacency matrix
class Graph4:
    def __init__(self, vrtCnt):
        self.adjMat = [[-1]*vrtCnt for x in range(vrtCnt)]
        self.vertices = {x for x in range(vrtCnt)}
        self.vrtCnt = vrtCnt

    def add_vertex(self):
        self.vertices.add(self.vrtCnt)
        self.vrtCnt += 1
        for adjacencies in self.adjMat:
            adjacencies.append(-1)
        self.adjMat.append([-1]*self.vrtCnt)
        print('Vertex {0} added.'.format(self.vrtCnt-1))

    def add_edge(self, vrtFrom, vrtTo, weight=0):
        self.adjMat[vrtFrom][vrtTo] = weight
        print('Edge from {0} to {1} of weight {2} added.'.format(vrtFrom, vrtTo, weight))

    def print_vertices(self):
        print('-'*50)
        print('Printing vertices...')
        print(self.vertices)
        print('-'*50)

    def print_edges(self):
        print('-'*50)
        print('Printing edges...')
        for vrtFrom in range(self.vrtCnt):
            for vrtTo in range(self.vrtCnt):
                if self.adjMat[vrtFrom][vrtTo] != -1:
                    print((vrtFrom, vrtTo, self.adjMat[vrtFrom][vrtTo]))
        print('-'*50)


testGraph = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
'''
graph = Graph1(testGraph)
graph.print_vertices()
graph.print_edges()

graph.add_vertex('f')
graph.add_edge('f', 'e')
graph.add_edge('f', 'b')

graph.print_vertices()
graph.print_edges()
'''

'''
graph2 = Graph2(testGraph)
graph2.print_vertices()
graph2.print_edges()

graph2.add_vertex('f')
graph2.add_edge('f', 'e')
graph2.add_edge('f', 'b')

graph2.print_vertices()
graph2.print_edges()
'''
'''
graph3 = Graph3(5)
graph3.print_vertices()
graph3.print_edges()

graph3.add_edge(0, 1, 10)
graph3.add_edge(1, 2, 20)
graph3.add_edge(2, 3, 30)
graph3.add_edge(3, 4, 40)

graph3.print_vertices()
graph3.print_edges()

graph3.add_vertex()
graph3.add_vertex()
graph3.add_edge(4, 5, 50)
graph3.add_edge(5, 6, 60)

graph3.print_vertices()
graph3.print_edges()
'''
graph4 = Graph4(5)
graph4.print_vertices()
graph4.print_edges()

graph4.add_edge(0, 1, 10)
graph4.add_edge(1, 2, 20)
graph4.add_edge(2, 3, 30)
graph4.add_edge(3, 4, 40)

graph4.print_vertices()
graph4.print_edges()

graph4.add_vertex()
graph4.add_vertex()
graph4.add_edge(4, 5, 50)
graph4.add_edge(5, 6, 60)

graph4.print_vertices()
graph4.print_edges()