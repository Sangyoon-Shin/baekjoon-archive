import sys
input = sys.stdin.readline
import heapq

minheap = []

n = int(input())

for i in range(n):
    x = int(input())
    if x == 0:  
        if len(minheap) == 0:
            print(0)
        else:
            k = heapq.heappop(minheap)
            print(k)

    else:
        heapq.heappush(minheap, x)
