import sys
input = sys.stdin.readline

coin, value = map(int, input().split())

category = []

for i in range(coin):
    a = int(input())
    category.append(a)

category.sort(reverse=True)

cnt = 0

for coinvalue in category:
    if coinvalue <= value:
        cnt = cnt + (value // coinvalue)
        value = value % coinvalue

print(cnt)


