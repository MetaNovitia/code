def f(a,b):
	if a[1]==b[1]: return a[0]>b[0]
	return a[1]<b[1]
n,k = input().split()
l = [[int(x) for x in input().split()] for i in range(int(n))]
l = sorted(l,reverse=True)
l = sorted(l,key = lambda t: t[1])
#print(l)
curr = 0
ans = 0
for x in range(int(k)):
	if x > l[curr][1]:
		ans += l[curr][0]
		curr += 1
	else: 
print(ans)
