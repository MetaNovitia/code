a=list(map(int,input().split()))
b=list(map(int,input().split()))
s1=s2=0
for i in range(3):
    s1+=a[i]>b[i]
    s2+=a[i]<b[i]
print(s1,s2,end="")
