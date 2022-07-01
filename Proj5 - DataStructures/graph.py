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

testGraph = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}

graph = Graph1(testGraph)
graph.print_vertices()
graph.print_edges()

graph.add_vertex('f')
graph.add_edge('f', 'e')
graph.add_edge('f', 'b')

graph.print_vertices()
graph.print_edges()