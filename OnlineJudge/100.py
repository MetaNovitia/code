###   UVA #100 : The 3n + 1 problem
###   Labels   : recursion, hashing, dp

import sys

table = {}
table[1] = 1

# build table as needed by the test cases
def makeTable(index):
    if index not in table: 
        if index%2: table[index]=makeTable(3*index+1)+1
        else:       table[index]=makeTable(int(index/2))+1
    return table[index]

for line in sys.stdin:
    i,j = [int(x) for x in line.split()]
    k = min(i,j)
    l = max(i,j)
    m = 0
    while k<=l:
        if k not in table: 
            table[k] = makeTable(k)
        m = max(table[k],m)
        k+=1
    print(i,j,m)
    