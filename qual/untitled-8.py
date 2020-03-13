n = int(input())

for _ in range(n):
    d={}
    a = input()
    words = []
    for l in range(len(a)):
        words.append([0 for _ in range(26)])
        for i in range(l+1):
            words[i][ord(a[l])-ord("a")]+=1
            r = ""
            for le in range(26):
                for _ in range(words[i][le]):
                    r+=chr(le+ord("a"))
            if r not in d or d[r][1]>i:
                d[r]=(i,l)
                
    res = [9999,10000]
    
    b = input()
    for l in range(len(b)):
        c = [0 for _ in range(26)]
        for i in range(l,len(b)):
            c[ord(b[i])-ord("a")]+=1
            r = ""
            for le in range(26):
                for _ in range(c[le]):
                    r+=chr(le+ord("a"))
            if r in d and (len(r)>res[0]-res[1]+1 or ((len(r)==res[0]-res[1]+1) and d[r][0]<res[1])):
                res[0] = d[r][1]
                res[1] = d[r][0]
    if res[0]-res[1]>-1: print(a[res[1]:res[0]+1])
    else: print("NONE")
    
"""
agofourscoreandsdsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagoforeandsevenyearsagodsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagfourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreandsevenyearsagofourscoreand
"""