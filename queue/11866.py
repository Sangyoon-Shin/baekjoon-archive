from collections import deque

arr = deque()
ans = []

n, k = map(int, input().split())

for i in range(n):
    arr.append(i + 1)

cnt = 0
while(len(arr) > 0):
    cnt += 1
    if cnt % k == 0:
        ans.append(str(arr.popleft()))
    else:
        arr.append(arr.popleft())

result = ", ".join(ans)
print('<', end='')
print(result, end='')
print('>')

