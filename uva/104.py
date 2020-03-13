###   UVA #104 : Arbitrage
###   Labels   : graph traversals

import sys
    
for n in sys.stdin:
    n = int(n)
    graph = [[float(x) for x in input().split()] for _ in range(n)]
    for i in range(n): graph[i].insert(i,1)
    queue = []
    ans = []
    for i in range(n):
        for j in range(n):
            if i!=j and graph[i][j]>=1:
                queue.append([[i,j],graph[i][j]])
                
    while queue!=[]:
        
        front = queue.pop(0)
        sequence = front[0]
        i = sequence[-1]
        start = sequence[0]
        curr = front[1]
        
        if len(sequence)==20:
            break
        
        for j in range(n):
            if i!=j and graph[i][j]*curr>=1:
                if start==j and graph[i][j]*curr>=1.01:
                    ans = sequence+[j]
                    queue = []
                    break
                queue.append([sequence+[j],graph[i][j]*curr])
                
    if ans!=[]:
        print("".join([' '+str(x) for x in ans])[1:])
    else:
        print("no arbitrage sequence exists")