n=int(input())
l=list(map(int,input().split()))
m=max(l)
ans=0
for i in l: 
    if i==m:ans+=1
print(ans,end="")
