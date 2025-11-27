import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)

for i in range(m):
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    add = x + y
    heapq.heappush(card, add)
    heapq.heappush(card, add)

total = 0
while card:
    total += heapq.heappop(card)

print(total)


