import sys
input = sys.stdin.readline

n, b, h, w = map(int, input().split())
mincost = 500001
budget = 0
flag = False

for i in range(h):
    p = int(input())
    canstay = list(map(int, input().split()))

    for limit in canstay:
        if n <= limit and limit >= 1:
            budget = n * p
            if budget <= b and budget <= mincost:
                mincost = budget
                flag = True

if flag:
    print(mincost)
else:
    print('stay home')