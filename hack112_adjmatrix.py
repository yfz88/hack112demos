from collections import defaultdict 
class Graph:
    # Initalize default dict -->: key: node, value: list of size numberOfNodes signifying value of edge between node 
    def __init__(self, numberOfNodes, edges):
        self.graph = defaultdict(lambda: [False] * numberOfNodes)
        for edge in edges:
            first, second = edge
            self.graph[first][second] = True
            self.graph[second][first] = True
    
    def hasNode(self, node):
        if node in self.graph:
            return True
        return False

    def hasEdge(self, edge): 
        first, second = edge
        return (self.graph[first][second] and self.graph[second][first])

    def insertNode(self, node, neighbors): 
        if node in self.graph:
            return

        # Create new row for matrix
        self.graph[node]
        # Add a new column
        for row in self.graph.values():
            row.append(False)
        
        for neighbor in neighbors:
            self.graph[node][neighbor] = True
            self.graph[neighbor][node] = True
        return
        
    def removeNode(self, removalNode): 
        # remove the node from the rows
        if removalNode in self.graph:
            del self.graph[removalNode]
        
        # remove the node from its neighbors
        for neighbor in self.graph:
            if removalNode < len(self.graph[neighbor]):
                self.graph[neighbor].pop(removalNode)
        
        return 
    
    def createEdge(self, edge): 
        first, second = edge
        self.graph[first][second] = True
        self.graph[second][first] = True
        return
    
    def removeEdge(self, edge): 
        first, second = edge
        self.graph[first][second] = False
        self.graph[second][first] = False
        return 
    


        

        
