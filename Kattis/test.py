from math import factorial

def npr(n, r):
    return factorial(n)/factorial(n-r)

n,k = [int(x) for x in input().split()]
words = sorted([input() for _ in range(n)])
target = input()
notTaken = [i-1 for i in range(n+1)]


order = [0 for _ in range(k)]

pos = 0
ct = 0
    
while pos<len(target):
    
    start = 0
    end = n
    i = int((start+end)/2)
    
    t = target[pos:min(pos+len(words[i]), len(target))]
               
    while words[i] != t:
        if t<words[i]:
            end = i-1
        else:
            start = i+1
        i = int((start+end)/2)
        t = target[ pos : min(pos+len(words[i]), len(target)) ]
      
    order[ct] = i+1
    ct+=1   
    pos += len(t)
    

ans = 1

for i in range(len(order)):
    ans += (notTaken[order[i]])*npr(n-i-1,k-i-1)
    for j in range(order[i]+1,n+1):
        notTaken[j]-=1
        
print(int(ans%(1E9+7)))