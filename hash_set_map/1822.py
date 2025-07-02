import sys
input = sys.stdin.readline

na, nb = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dicta = {}
dictb = {}

for i in a:
    if i not in dicta.keys():
        dicta[i] = 1
    else:
        dicta[i] += 1

for i in b:
    if i not in dictb.keys():
        dictb[i] = 1
    else:
        dictb[i] += 1

res = []

for i in dicta.keys():
    if i not in dictb.keys():
        res.append(i)

res.sort()
print(len(res))

if len(res) == 0:
    pass
else:
    print(*res)


