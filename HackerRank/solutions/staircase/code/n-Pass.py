n=int(input())
for i in range(n):
    print((" "*(n-i-1))+("#"*(i+1)),end="")
    if i!=n-1:print()
