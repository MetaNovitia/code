# K
t = int(input())
for _ in range(t):
    n  = int(input())
    d = {}
    for i in range(n):
        x,y = input().split()
        if x not in d: d[x] = 0
        d[x] += int(y)
    print(len(list(d)))
    l = sorted([(-d[x],x) for x in d])
    for x in l:
        print(x[1], -x[0])