from collections import deque

router = deque()

n = int(input())
cnt = 0

while(1):
    k = int(input())
    if k == -1:
        if len(router) != 0:
            print(*router, end=' ')
            break
        else:
            print("empty")
            break

    elif k == 0:
        router.popleft()
        cnt -= 1

    else:
        if(cnt < n):
            router.append(k)
            cnt += 1
        else:
            continue
