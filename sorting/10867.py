import sys
input = sys.stdin.readline

arr = set()

n = int(input())

k = list(map(int, input().split()))

for i in k:
    arr.add(i)

arr = list(arr)
arr.sort()
print(*arr)