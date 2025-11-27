import sys
import heapq
input = sys.stdin.readline

position = [[] for i in range(11)]

n, k = map(int, input().split())
for i in range(n):
    pos, value = map(int, input().split())
    heapq.heappush(position[pos - 1], -value)

teamvalue = 0
for i in range(k):
    for j in range(len(position)):
        if not position[j]:
            continue
        best = -heapq.heappop(position[j])
        if best > 0:
            best -= 1
        heapq.heappush(position[j], -best)

for i in range(len(position)):
    if len(position[i]):
        teamvalue += -heapq.heappop(position[i])

print(teamvalue)    
