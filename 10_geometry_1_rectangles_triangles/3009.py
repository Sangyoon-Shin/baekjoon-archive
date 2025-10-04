xlist = []
ylist = []

for i in range(3):
    x, y = map(int, input().split())
    if x in xlist:
        xlist.remove(x)
    else:
        xlist.append(x)
    if y in ylist:
        ylist.remove(y)
    else:
        ylist.append(y)
    
print(xlist[0], ylist[0])