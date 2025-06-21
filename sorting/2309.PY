import sys
from itertools import combinations
input = sys.stdin.readline

idxmap = {}

for i in range(9):
    idxmap[i] = int(input())

comlist = list(combinations(idxmap.keys(), 7))

flag = 0
for i in range(len(comlist)):
    if flag == 1:
        break
    sum = 0
    ans = []
    for k in range(7):
        sum = sum + idxmap[comlist[i][k]]
        ans.append(idxmap[comlist[i][k]])
    if sum == 100:
        flag = 1
        break

ans.sort()
print(*ans)
        

