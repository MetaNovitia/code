def main():
	n,k = map(int,input().split())
	xq,yq = map(int,input().split())

	"""
	blocks: distance queen can travel in a direction
			clockwise order from top
			assume origin is bottom left 
	"""
	blocks = [n-yq, 0, n-xq, 0, yq-1, 0, xq-1, 0]
	for i in range(1,8,2): 
		blocks[i] = min(blocks[i-1],blocks[(i+1)%8])

	while k:
		x,y = map(int,input().split())
		rise = y - yq
		run = x - xq
		if (run == 0):            	# vertical case
			b_i = 0 if (rise > 0) else 4
			blocks[b_i] = min(blocks[b_i], abs(rise)-1)
		elif (rise == 0):      		# horizontal case
			b_i = 2 if (run > 0) else 6
			blocks[b_i] = min(blocks[b_i], abs(run)-1)
		elif (rise == run):    		# positive gradient
			b_i = 1 if (run > 0) else 5
			blocks[b_i] = min(blocks[b_i], abs(run)-1)
		elif (rise == -run):   		# negative gradient
			b_i = 3 if (run > 0) else 7
			blocks[b_i] = min(blocks[b_i], abs(run)-1)
		k-=1

	print(sum(blocks))

# Code Golf of O(n) (253 bytes):
import sys;n,k,a,b,*q=map(int,sys.stdin.read().split());e=min;n+=1;r=[a,n-a,b,n-b,e(b,a),e(n-b,n-a),e(a,n-b),e(n-a,b),-8,0]
while k:p,o=q.pop()-b,q.pop()-a;c=o>0;j=[(p==0)*4+6*(p==o)+8*(p==-o)+c-2,p>0][o==0];r[j]=e(-e(o,p,-o,-p),r[j]);k-=1
print(sum(r))