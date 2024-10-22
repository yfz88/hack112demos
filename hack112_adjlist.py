class Graph:
    def __init__(self, numberOfNodes, edges): 
        self.graph = dict()
        for i in range(1, numberOfNodes + 1): 
            self.graph[i] = set()
        
        # Add all neighbors to corresponding node
        for edge in edges: 
            node, neighbor = edge
            self.graph[node].add(neighbor)
        return 

    def hasNode(self, node): 
        if node in self.graph:
            return True
        return False

    def hasEdge(self, a, b): 
        return (b in self.graph[a] and a in self.graph[b])

    # neighbors --> [List]: list of neighbor nodes
    # node --> int represented number of node being inserted
    def insertNode(self, node, neighbors): 
        if node in self.graph: 
            return
        
        # Add node in all of it's connections
        for neighbor in neighbors: 
            self.graph[neighbor].add(node)
        
        # Add the node itself with the given connections
        self.graph[node] = set(neighbors)
        return
        
    def removeNode(self, removalNode): 
        if removalNode not in self.graph:
            return 
        
        for vertex in self.graph:
            if removalNode in self.graph[vertex]: 
                self.graph[vertex].remove(removalNode)
        
        del self.graph[removalNode]
        return

    # edge  --> tuple representing edge between two nodes
    def createEdge(self, edge):
        first, second = edge
        self.graph[first].add(second)
        self.graph[second].add(first)
        return
    
    # edge  --> tuple representing edge to remove
    def removeEdge(self, edge):
        first, second = edge
        self.graph[first].remove(second)
        # Can check if node has remaining neighbors and remove accordingly
        self.graph[second].remove[first]
        # Can check if node has remaining neighbors and remove accordingly
        return





    
