###   UVA #168 : Theseus and the Minotaur
###   Labels   : Graph Traversal

line = input().split()
while line!=['#']:
    minotaur = line[1]
    k = int(line[3])
    light = [line[2]]

    graph = { x.split(':')[0]: x.split(':')[-1]
             for x in line[0][:-1].split(";") 
             if len(x.split(':'))==2 and x.split(':')[-1]!=""}
    ct = 0
    
    while minotaur in graph:
        destinations = graph[minotaur]
        for dest in destinations:
            if dest not in light:
                ct+=1
                if ct==k:
                    ct=0
                    print(minotaur, end=' ')
                    light.append(minotaur)
                light[0] = minotaur
                minotaur = dest
                
                break
        else:
            print('/' + minotaur)
            break    
    else:
        print('/' + minotaur)
        
    line = input().split()
