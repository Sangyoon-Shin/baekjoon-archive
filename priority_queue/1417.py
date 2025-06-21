import sys
import heapq
input = sys.stdin.readline

candidate = []

n = int(input())
for i in range(n):
    k = int(input())
    heapq.heappush(candidate, -k)

maximum = -heapq.heappop(candidate)

while True:
    if  