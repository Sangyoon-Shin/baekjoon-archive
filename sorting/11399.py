import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
heap = []

for i in arr:
    heapq.heappush(heap, i)

sum = 0
total = 0

for i in range(len(heap)):
    sum = sum + heapq.heappop(heap)
    total = total + sum

print(total)