import sys
input = sys.stdin.readline

money, count = map(int, input().split())
total = money
rest = money // count
while True:
    if rest < count:
        total += rest
        break
    else:
        total += rest
        rest = rest // count
print(total)