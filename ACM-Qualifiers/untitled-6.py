p0 = [(440,"A")]
note = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
conv = {"D#":"Eb","G#":"Ab","A#":"Bb"}

chords = [
    [1,["G","A","B","C","D","E","F#"],"G major"],
    [1,["C","D","E","F","G","A","B"],"C major"],
    [2,["D#","F","G","G#","A#","C","D"],"Eb major"],
    [1,["F#","G#","A","B","C#","D","E"],"F# minor"],
    [2,["G","A","A#","C","D","D#","F"],"G minor"]
]
ct=1

div = 2 ** (1/12)

while p0[-1][0] < 830:
    p0.append((p0[-1][0]*div,note[ct]))
    ct+=1
    
d = {}
for nt in p0:
    d[f"%.4f" %nt[0]] = nt[1]
    curr = nt[0]
    while curr <= 4000:
        curr *= 2
        d[f"%.4f" %curr] = nt[1]
    curr = nt[0]
    while curr >= 20:
        curr /= 2
        d[f"%.4f" %curr] = nt[1]

n = int(input())
res = []
ct = 0
for _ in range(n):
    f = f"%.4f" %float(input())
    res.append(d[f])
    for i in range(5):
        if chords[i][0]!=0 and d[f] not in chords[i][1]:
            chords[i][0] = 0
            ct+=1
            
if ct!=4: print("cannot determine key")
else:
    pos = -1
    for i in chords:
        if i[0]:
            pos = i[2]
    
            print(pos)
            if i[0] == 1:
                for letter in res: print(letter)
            else:
                for letter in res: 
                    if letter in conv: print(conv[letter])
                    else: print(letter)
