import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(i + 1)

for j in permutations(arr, m):
    print(*j)


