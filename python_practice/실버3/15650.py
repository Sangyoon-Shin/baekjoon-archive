import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
ans = []

for i in range(n):
    arr.append(i + 1)

for j in combinations(arr, m):
    ans.append(j)

ans.sort(key=lambda x:x[0])

for i in ans:
    print(*i)



