import sys
import heapq
input = sys.stdin.readline

# 메모리 624072 KB, 시간 3616 ms 
# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# a.sort()
# print(a[k - 1])

# 7284 ms. heap 쓰면 시간 두배?
minheap = []
n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    heapq.heappush(minheap, i)

for j in range(k - 1):
    heapq.heappop(minheap)

print(heapq.heappop(minheap))