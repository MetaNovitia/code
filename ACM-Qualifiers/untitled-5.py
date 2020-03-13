import math
from collections import defaultdict 

class Graph: 

    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = []


    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def KruskalMST(self): 

        result =[] 

        i = 0
        e = 0
        
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 

        parent = [] ; rank = [] 

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 

        while e < self.V -1 : 

            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
        
        sm = 0
        for i in result: sm+= i[2]
        return sm

n = int(raw_input())
l = [[int(x) for x in raw_input().split()] for _ in range(n)]
g = Graph(n)

for i in range(n-1):
    for j in range(i+1,n):
        g.addEdge(i,j, math.sqrt( ((l[i][0]-l[j][0]) * (l[i][0]-l[j][0])) + ((l[i][1]-l[j][1]) * (l[i][1]-l[j][1]) ) ) - l[i][2] - l[j][2] )


print(g.KruskalMST())