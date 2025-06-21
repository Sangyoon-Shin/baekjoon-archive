import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    rank = list(map(int, input().split()))
    arr = deque(rank)
    idx = deque(i for i in range(n))

    if n == 1:
        print(1)
    else:
        cnt = 1
        while(1):
            max_v = max(arr)
            if(arr[0] >= max_v):
                arr.popleft()
                order = idx.popleft()
                if(order == m):
                    print(cnt)
                    break
                else:
                    cnt += 1
            else:
                arr.append(arr.popleft())
                idx.append(idx.popleft())





