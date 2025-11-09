import sys
import heapq
input = sys.stdin.readline

n = int(input())
snow = map(int, input().split())

# 항상 시간이 오래 남은 두 집을 뽑고, 눈을 치우면서 순서가 계속 바뀌기 때문에 우선순위 큐 사용
maxheap = []
time = 0

for i in snow:
    heapq.heappush(maxheap, -i)

# 만약에 힙에 두 개 이상 남아있으면 두개를 다 뽑는게 시간 덜 듦
# 뽑은 애들을 하나씩 빼주고 그 값이 0이 아니면 다시 힙에 집어넣기. 그러면 계속해서 시간이 오래남은 2개를 우선적으로 뽑을 수 있음.
while len(maxheap) >= 2:
    first = -heapq.heappop(maxheap)
    second = -heapq.heappop(maxheap)
    time += 1
    first -= 1
    second -= 1
    if first > 0:
        heapq.heappush(maxheap, -first) 
    if second > 0:
        heapq.heappush(maxheap, -second)

# 끝나고 1개가 남아있거나 비어있거나 둘 중 하나. 남아있으면 걔를 다 처리해줘야함
if maxheap:
    time += -heapq.heappop(maxheap)

if time > 1440:
    print(-1)
else:
    print(time)





