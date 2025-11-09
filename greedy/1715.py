import sys
import heapq
input = sys.stdin.readline

# 제일 작은 묶음 두 개씩을 선택(minheap 사용)하고, 그 두 묶음을 더한 새로운 묶음도 크기 비교에 사용해야함. -> 우선순위 큐 사용하기
n = int(input())
minheap = []

for i in range(n):
    num = int(input())
    heapq.heappush(minheap, num)

res = 0
while len(minheap) >= 2:
    a = heapq.heappop(minheap)
    b = heapq.heappop(minheap)
    res += a + b
    heapq.heappush(minheap, a + b)

print(res)
