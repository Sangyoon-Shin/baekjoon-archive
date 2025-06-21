import sys
import heapq
input = sys.stdin.readline

minheap = []

n = int(input())

for i in range(n):
    x = int(input())
    if x == 0:
        if len(minheap) == 0:
            print(0)
        else:
            x, y = map(int, heapq.heappop(minheap))
            print(y)
    else:
        heapq.heappush(minheap, (abs(x), x))

