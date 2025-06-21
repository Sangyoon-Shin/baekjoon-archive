from collections import deque

q = deque()
drop = deque()

n = int(input())

for i in range(n):
    q.append(i + 1)

while(len(q) > 1):
    drop.append(q.popleft())
    q.append(q.popleft())

for i in range(len(drop)):
    print(drop[i], end=' ')

print(q[0]) 
