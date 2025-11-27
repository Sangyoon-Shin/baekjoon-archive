import sys
import heapq
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
giftcount = list(map(int, input().split()))
gift = []

for i in giftcount:
    heapq.heappush(gift, -i)

want = deque(list(map(int, input().split())))

while want:
    child = want.popleft()
    if gift:
        cur = -heapq.heappop(gift)
        if child < cur:
            cur -= child
            heapq.heappush(gift, -cur) # 남은 건 다시 넣어주고
        elif child == cur:
            -heapq.heappop(gift) # 딱 맞는 개수면 그냥 뽑고
        else:
            print(0) # 못 가져가면 0 출력하고 끝
            sys.exit()
    else:
        # 선물 받을 애들은 남아있는데 선물이 없으면 0 출력하고 끝
        print(0)
        sys.exit()

print(1)    






