import sys
input = sys.stdin.readline

n, m = map(int, input().split())

narr = set()
marr = set()
xarr = []

for i in range(n):
    name = input().strip()
    narr.add(name)

for j in range(m):
    name = input().strip()
    marr.add(name)

cnt = 0

for i in marr:
    if i in narr:
        cnt += 1
        xarr.append(i)  

print(cnt)
xarr.sort()
for i in range(len(xarr)):
    print(xarr[i])   




