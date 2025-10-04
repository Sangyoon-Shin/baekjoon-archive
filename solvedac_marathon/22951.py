from collections import deque
import sys
input = sys.stdin.readline

numarr = deque()
orderarr = deque()

n, k = map(int, input().split())
for i in range(n):
    numarr.extend(list(map(int, input().split())))
    orderarr.extend([i + 1] * k)

while True:
    if len(numarr) == 1:
        print(orderarr[0], numarr[0])
        break
    else:
        num = numarr.popleft()
        orderarr.popleft()
        for i in range(num - 1):
            numarr.rotate(-1)
            orderarr.rotate(-1)
