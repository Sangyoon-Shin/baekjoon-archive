import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = {}

for i in range(n):
    item, price = input().strip().split()
    price = int(price)
    info[item] = price + (price * 0.05)

cnt = 0
for i in range(m):
    item, price = input().strip().split()
    price = int(price)
    if price > info[item]:
        cnt += 1

print(cnt)
