n,m = [int(x) for x in input().split()]

adj = {i:[[],-1] for i in range(1,n+1)}

for _ in range(m):
    x,b = [int(x) for x in input().split()]
    a = abs(x)
    
    if x<0: adj[a][1] = b
    else: adj[a][0].append(b)

visited = set()

q = [(1,0)]

result = set()
while len(q):
    top,state = q.pop(0)
    forced = adj[top][1]
    if forced == -1:
        result.add(top)
    elif forced not in visited:
        visited.add(forced)
        q.append((forced,state))
    
    if state==0:
        for node in adj[top][0]:
            visited.add(node)
            q.append((node,1))

print(len(result))