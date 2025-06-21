from collections import deque

circle = deque()
ans = list()
cnt = 1

n, k = map(int, input().split())

for i in range(n):
    circle.append(i + 1)

while(len(circle) > 0):
    if (cnt % k) == 0:
        ans.append(circle.popleft())
    else:
        circle.append(circle.popleft())
    cnt += 1

idx = 0
print('<', end='')
for i in range(len(ans)):
    if idx != len(ans) - 1:
        print(str(ans[i]) + ', ', end='')
    else:
        print(str(ans[i]) + '>', end='')
    idx += 1