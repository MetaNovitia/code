import sys;n,k,a,b,*q=map(int,sys.stdin.read().split());e=min;n+=1;r=[a,n-a,b,n-b,e(b,a),e(n-b,n-a),e(a,n-b),e(n-a,b),-8,0]
while k:p,o=q.pop()-b,q.pop()-a;c=o>0;j=[(p==0)*4+6*(p==o)+8*(p==-o)+c-2,p>0][o==0];r[j]=e(-e(o,p,-o,-p),r[j]);k-=1
print(sum(r))