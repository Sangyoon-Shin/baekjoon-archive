import sys
input = sys.stdin.readline

n = int(input())
price = []
for i in range(n):
    price.append(int(input()))

price.sort(reverse=True)

start = 0
total = 0
while True:
    if start == len(price):
        break
    elif start + 3 <= len(price):
        cur = price[start:start + 3]
        total += cur[0] + cur[1]
        start += 3
    else:
        total += price[start]
        start += 1

print(total)
        


