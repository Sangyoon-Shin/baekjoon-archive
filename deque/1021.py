import sys
from collections import deque
input = sys.stdin.readline

q = deque()

n, m = map(int, input().split())
idxs = deque(map(int, input().split()))

for i in range(n):
    q.append(i + 1)

cnt = 0
for idx in idxs:
    while True:
        if q[0] == idx:
            q.popleft()
            break
        
        else:
            if q.index(idx) < len(q)/2: # 오른쪽으로 이동해야 하는 경우
                while q[0] != idx:
                    q.append(q.popleft())
                    cnt +=1
            else:
                while q[0] != idx:      # 왼쪽으로 이동해야 하는 경우
                    q.appendleft(q.pop())
                    cnt += 1

print(cnt)



