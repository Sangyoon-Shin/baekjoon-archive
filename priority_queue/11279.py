import sys
input = sys.stdin.readline
import heapq

maxheap = []

n = int(input())

for i in range(n):
    x = int(input())
    if x == 0:
        if len(maxheap) == 0:
            print(0)
        else:
            k = -heapq.heappop(maxheap)
            print(k)

    else:
        heapq.heappush(maxheap, -x)