###   UVA #102 : Ecological Bin Packing
###   Labels   : bin packing

import sys

key = {0:'B', 1:'G', 2:'C'}

for line in sys.stdin:
    l = [int(x) for x in line.split()]
    total = sum(l)
    max_unchanged = 0
    max_string = "GGG"
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i!=j and j!=k and k!=i:
                    curr_unchanged = l[i]+l[3+j]+l[6+k]
                    curr_string = key[i]+key[j]+key[k]
                    if curr_unchanged > max_unchanged or ( curr_unchanged == max_unchanged and curr_string < max_string):
                        max_unchanged = curr_unchanged
                        max_string = curr_string
                        
    print( max_string + " " + str(total-max_unchanged) )