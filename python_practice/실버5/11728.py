import sys
input = sys.stdin.readline

arr = []
n, m = map(int, input().split())

k = list(map(int, input().split()))
for _ in k:
    arr.append(_)

k = list(map(int, input().split()))
for _ in k:
    arr.append(_)

arr.sort()
print(*arr)