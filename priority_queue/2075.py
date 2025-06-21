import sys
import heapq
input = sys.stdin.readline

n = int(input())

minheap = []

for i in range(n):
    x = list(map(int, input().split()))
    for j in range(n):
        if len(minheap) >= n:
            if x[j] > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, x[j])
            else:
                pass

        else:
            heapq.heappush(minheap, x[j])

print(minheap[0])



# 최소힙에 입력 받고 시작.
# 그 다음 입력 n개에 대해서 최소힙에 저장되어 있던 min[0] 값 보다
# 입력값이 크면 min[0]을 버리고 입력값 push 