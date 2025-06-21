import heapq

n = input()
arr = []

for i in range(len(n)):
    heapq.heappush(arr, -(int(n[i])))

for i in range(len(arr)):
    print(-heapq.heappop(arr), end='')