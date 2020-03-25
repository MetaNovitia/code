t=int(input())
l=map(int,input().split())
p=n=z=0
for i in l:
    p+=i>0
    n+=i<0
    z+=i==0
print(f"{p/t:.6f}\n{n/t:.6f}\n{z/t:.6f}",end="")
