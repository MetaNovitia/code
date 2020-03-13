###   UVA #105 : The Skyline Problem
###   Labels   : Brute Force, implementation

import sys
city = []
temp_city = []
for line in sys.stdin:
    left,height,right = [int(x) for x in line.split()]
    
    ### get rid if current building encloses last building
    while city!=[] and height > city[-1][1] and city[-1][0]>=left: 
        if city[-1][2]>right:
            temp_city.append([max(city[-1][0],right),city[-1][1],city[-1][2]])
        city.pop()
    
    ### when city is empty
    if city==[]: city.append([left,height,right])
    
    ### when previous building is taller than current
    elif height < city[-1][1] and right>city[-1][2]:
        
        # cut until right side of previous building
        city.append([max(left,city[-1][2]),height,right])
        
    ### when previous building is shorter than current, but current does not enclose previous builing
    elif height > city[-1][1]:
        
        # if previous building is longer (left and right) than current
        if city[-1][2]>right:
            temp_city.append([right,city[-1][1],city[-1][2]])        
        
        # change right bound, then add new building
        city[-1][2] = min(left,city[-1][2])
        city.append([left,height,right])
        
    ### when previous and current building has equal heights
    elif height == city[-1][1]:
        
        # extend right bound
        city[-1][2] = max(right,city[-1][2])     
    
    if temp_city!=[]: 
        temp_city = sorted(temp_city)
        city+=temp_city
        temp_city=[]
        
for building in city:
    print(str(building[0]) + " " + str(building[1]), end=' ')
print(str(city[-1][2])+' 0')