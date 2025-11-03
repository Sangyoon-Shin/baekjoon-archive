import sys
from collections import deque
input = sys.stdin.readline

n, weight = map(int, input().split())
if n == 0:
    print(0)
    sys.exit(0)
book = deque(map(int, input().split()))
box = 1
cur = 0

while True:
    if len(book) == 0:  
        break
    else:
        b = book.popleft()
        if cur + b <= weight:
            cur += b
        else:
            box += 1
            cur = 0
            cur += b

if cur <= weight:
    pass
else:
    box += 1

print(box)





