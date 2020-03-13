from math import gcd

a, b = tuple(map(int, input().split()))
g=gcd(a,b)
if (a//g)%2==1 and (b//g)%2==1:print(g)
else: print(0)
