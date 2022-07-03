# -----
# -----
# Graphs
#https://www.tutorialspoint.com/python_data_structure/python_graphs.htm
#https://www.geeksforgeeks.org/python-data-structures/
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
        self.adjMat = [[0]*vrtCnt for x in range(vrtCnt)]
        self.vertices = {x for x in range(vrtCnt)}
        self.edges = set()
        self.vrtCount = vrtCnt
    
    def add_vertex(self):
        pass

    def add_edge(self):
        pass

    def print_vertices(self):
        print(self.vertices)

    def print_edges(self):
        pass

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