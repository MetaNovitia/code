###   UVA #280 : Vertex
###   Labels   : bfs

n = int(input())
while n!=0:
    graph = dict()
    edges = [int(x)-1 for x in input().split()[:-1]]
    while len(edges)>0:
        graph[edges[0]] = edges[1:]
        edges = [int(x)-1 for x in input().split()[:-1]]
    start_nodes = [int(x)-1 for x in input().split()[1:]]
    
    # bfs
    for node in start_nodes:
        visited = [0 for _ in range(n)]
        q = [node]
        while q!=[]:
            head = q.pop(0)
            if head in graph:
                for dest in graph[head]:
                    if not visited[dest]:
                        visited[dest] = 1
                        q.append(dest)

        s = ''
        s+= str(n-sum(visited))+" "
        for i in range(n):
            if not visited[i]:
                s+=str(i+1)+' '
        print(s[:-1])
    n = int(input())