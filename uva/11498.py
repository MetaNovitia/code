###   UVA #11498 : Division of Nlogonia
###   Labels     : ad hoc

k = int(input())
while k:
    (x,y) = [int(i) for i in input().split()]
    for _ in range(k):
        (a,b) = [int(i) for i in input().split()]
        print("divisa" if a==x or y==b else str("N"if b>y else"S")+str("E"if a>x else"O"))
    k = int(input())