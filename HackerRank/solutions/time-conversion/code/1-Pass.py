a=input()
h=int(a[:2])
if h==12: h-=12
if a[8]=="P": h+=12
print(f"{h:02d}"+a[2:8],end="")
