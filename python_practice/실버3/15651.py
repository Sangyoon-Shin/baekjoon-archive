import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
ans = []
sameans= []

for i in range(n):
    arr.append(i + 1)

for j in product(arr, repeat=m):
    ans.append(j)

ans.sort()

for k in ans:
    print(*k)



