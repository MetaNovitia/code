n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
s=0
for i in range(n):
    s+=m[i][i]
    s-=m[i][-i-1]
print(abs(s),end="")
