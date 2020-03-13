###   UVA #11172 : Relational Operator
###   Labels     : ad hoc

for _ in range(int(input())): 
    l = [int(x) for x in input().split()]
    print('>' if l[0]>l[1] else '<' if l[0]<l[1] else '=')