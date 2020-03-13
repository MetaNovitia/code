# F
n,q = [int(x) for x in input().split()]
pos = [int(x) for x in input().split()]
for _ in range(q):
    t,a,b = [int(x) for x in input().split()]
    if t==1:
        pos[a-1] = b
    else:
        print(abs(pos[a-1]-pos[b-1]))