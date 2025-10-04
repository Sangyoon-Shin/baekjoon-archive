import sys
import heapq
input = sys.stdin.readline

n = int(input())
gift = [] # 높은 숫자가 gift[0]에 위치하도록

for i in range(n):
    info = list(map(int, input().split()))
    if info[0] == 0:
        # 비어있으면 -1, 아니면 가장 가치가 높은값 뽑기
        if len(gift) == 0:
            print(-1)
        else:
            print(-heapq.heappop(gift))
    else:
        for i in range(info[0]):
            heapq.heappush(gift, -info[i + 1])
    

