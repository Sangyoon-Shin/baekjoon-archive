import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = list(map(int, input().split()))

arr = deque()
for i in range(n):
    arr.append((i + 1, k[i]))

ans = []

while len(arr) > 0:
    idx, val = arr.popleft()
    ans.append(idx)

    if val > 0:
        arr.rotate(-(val - 1)) # 오른쪽으로 이동한다는건 덱을 왼쪽으로 돌리는 것
    
    elif val < 0:
        val = abs(val)
        arr.rotate(val)

print(*ans)





