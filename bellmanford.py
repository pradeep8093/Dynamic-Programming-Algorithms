import sys
class Graph:

    def __init__(self,vertices,edges):
        self.V=vertices
        self.E=edges
        self.graph=[]

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def printdist(self,dist):

        for i in range(self.V):
        
                print("%d \t\t %d" % (i, dist[i]))

    def bellmanford(self):

        dist=[]
        parent=[]
        
        for i in range(self.V):
            dist.append(float("Inf"))
            parent.append(-1)

        dist[0]=0
        

        for i in range((self.V)-1):

            
            

            for u, v, w in self.graph:
                
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print "Graph contains negative weight cycle"
                return
        self.printdist(dist)

        

g = Graph(5,8)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
 
#Print the solution
g.bellmanford()     
    
