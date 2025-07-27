import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = set()

for i in permutations(arr, k):
    i = list(i)
    i = list(map(str, i))
    result = ''.join(i)
    res.add(result)

print(len(res))
