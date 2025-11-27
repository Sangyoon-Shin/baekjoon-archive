import sys
import heapq
input = sys.stdin.readline

n, centi, t = map(int, input().split())
giant = []

for i in range(n):
    height = int(input())
    heapq.heappush(giant, -height)

cnt = 0
for i in range(t):
    top = -heapq.heappop(giant)
    if top == 1 and centi == 1:
            print("NO")
            print(1)
            sys.exit(0)
    if top >= centi: 
        top //= 2
        heapq.heappush(giant, -top)
        cnt += 1
    else:
        print("YES")
        print(cnt)
        sys.exit(0)

if n == 1:
    k = -heapq.heappop(giant)
    if k >= centi:
        print("NO")
        print(k)
    else:
        print("YES")
        print(cnt)
else:
    f = -heapq.heappop(giant)
    if f >= centi:
        print("NO")
        print(f)
    else:
        print("YES")
        print(cnt)      
        
