import sys
input = sys.stdin.readline

n = int(input())
worddict = {}
res = []

for i in range(n):
    name = input().rstrip()
    name = name[name.index('.') + 1:]
    
    if name in worddict:
        worddict[name] += 1
    else:
        worddict[name] = 1
    
for i in worddict.keys():
    res.append((i, worddict[i]))

res.sort(key=lambda x: x[0])

for i in res:
    print(i[0], i[1])