n = int(input())

def rec(x,y,l,n):
    if l==1: return n
    nl = l>>1
    if n==0:
        if (x<l and y<nl) or (x<nl and y<l): return rec(x,y,nl,0)
        if (y>=nl*3) or (x<nl): return rec(x,y-l,nl,1)
        if (x>=nl*3) or (y<nl): return rec(x-l,y,nl,3)
        else: return rec(x-nl,y-nl,nl,0)
    if n==1:
        if (x<l and y>=nl*3) or (x<nl and y>=l): return rec(x,y-l,nl,1)
        if (y>=nl*3) or (x>=nl*3): return rec(x-l,y-l,nl,2)
        if (x<nl) or (y<nl): return rec(x,y,nl,0)
        else: return rec(x-nl,y-nl,nl,1)    
    if n==2:
        if (x>=l and y>=nl*3) or (x>=nl*3 and y>=l): return rec(x-l,y-l,nl,2)
        if (y>=nl*3) or (x<nl): return rec(x,y-l,nl,1)
        if (x>=nl*3) or (y<nl): return rec(x-l,y,nl,3)
        else: return rec(x-nl,y-nl,nl,2)
    if n==3:
        if (x>=l and y<nl) or (x>=nl*3 and y<l): return rec(x-l,y,nl,3)
        if (y>=nl*3) or (x>=nl*3): return rec(x-l,y-l,nl,2)
        if (x<nl) or (y<nl): return rec(x,y,nl,0)
        else: return rec(x-nl,y-nl,nl,3)    
            

for _ in range(n):
    x,y = [int(x) for x in input().split()]
    print(rec(x,y,1 << 60, 0))
    